<#

Raul Baptista de Souza
YYYY/MM/DD = 2022/03/17

.DESCRIPTION
This script is used for ...
--------------------------------------------------------
|Flag         | Description                            |
--------------------------------------------------------
|             |                                        |
--------------------------------------------------------

* 

.EXAMPLE
./PrepareData.ps1

.LINK
https://.../#documentation

#>

# param(
#     [parameter(ParameterSetName="help", Mandatory=$true)][switch]$help, 
#     [parameter(ParameterSetName="h", Mandatory=$true)][switch]$h
# )

# if(($PSCmdlet.ParameterSetName -eq 'help' -and $help) -or 
#     ($PSCmdlet.ParameterSetName -eq 'h' -and $h)) {
#     Get-Help $MyInvocation.MyCommand.Path -detailed
#     exit
# }


$columns = @('id','processDefinitionKey','processDefinitionId','minDurationInMillis', 'meanDurationInMillis', 'maxDurationInMillis', 'countInstance')
$AllIntColumns =  @('minDurationInMillis', 'meanDurationInMillis', 'maxDurationInMillis', 'countInstance')
function GetProcessIntancesMeasures($Columns){
    # Cria o processDefinitionId.json
    $csv = @()
    $data = curl -XGET camunda:8080/engine-rest/history/process-instance | ConvertFrom-Json
    $listProcessDefinitionId = ($data.processDefinitionId | Select-Object -Unique)
    foreach($process in $listProcessDefinitionId){
        $processesInstances = $data | Where-Object {$_.processDefinitionId -eq $process}
        $listDuration = @()
        $min, $mean, $max = 0, 0, 0
        $info = "" | Select-Object $columns
        foreach($instance in $processesInstances){
            if(![int]::IsNullOrEmpty -eq $instance.durationInMillis){
                $info.id = $instance.id
                $info.processDefinitionKey = $instance.processDefinitionKey
                $info.processDefinitionId = $instance.processDefinitionId
                $listDuration+= $instance.durationInMillis
            }
        }
        if(![int]::IsNullOrEmpty -eq $listDuration){
            $Measures = ($listDuration | Measure-Object -Average -Maximum -Minimum)
            $info.minDurationInMillis = $Measures.Minimum
            $info.meanDurationInMillis = $Measures.Average
            $info.maxDurationInMillis = $Measures.Maximum
            $info.countInstance = $Measures.Count
            $csv += $info
        }
    }
    return $csv
}

function CreateDataJson($csvImport, $Columns){
    $csv = @()
    foreach ($row in $csvImport) {
        $data = $row
        $index = Get-Content '.\indexPatten.json' | ConvertFrom-Json
        $index.index._id = $data.id

        $csv+= $index
        foreach($column in $Columns){
            $data.$column = [int]$data.$column
        }
        $csv+= $data
    }
    $csv = $csv | Select-Object -Property * -ExcludeProperty id
    return $csv
}

function bulkJson($json){
    $file = $json
    $file = $file.Substring(1,$file.length-2)
    $bulk = ""
    while($file -match ',{'){
        $index = $file.IndexOf(',{')
        $lastIndex = $file.length - 1
        $bulk += $file.Substring(0,$index) + "`n"
        $file = $file.Substring($index + 1)
    }
    $bulk += $file
    $bulk | Out-File "bulk.json" # -Encoding utf8BOM
}

@(GetProcessIntancesMeasures -Columns $columns) | Select-Object $columns | Export-CSV -NoTypeInformation "./ProcessIntancesMeasures.csv"

$csv = @(GetProcessIntancesMeasures -Columns $columns)
$json = @(CreateDataJson -csvImport $csv -Columns $AllIntColumns) | ConvertTo-Json -Depth 100 -Compress
bulkJson -jsonImport -json $json

