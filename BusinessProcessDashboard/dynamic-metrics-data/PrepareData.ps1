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


$columnsProcess = @('processDefinitionKey','processDefinitionId','processDefinitionVersion','minProcessDurationInMillis','meanProcessDurationInMillis','maxProcessDurationInMillis','countProcessInstance')
$columnsTask = @('processDefinitionKey','processDefinitionId','processDefinitionVersion','taskName','minTaskDurationInMillis','meanTaskDurationInMillis','maxTaskDurationInMillis','countTaskInstance')

function GetProcessIntancesMeasures($Columns){
    $csv = @()
    $data_ProcessInstance = curl -XGET camunda:8080/engine-rest/history/process-instance?finished=true | ConvertFrom-Json
    $listProcessDefinitionId = ($data_ProcessInstance.processDefinitionId | Select-Object -Unique)
    foreach($process in $listProcessDefinitionId){
        $processesInstances = $data_ProcessInstance | Where-Object {$_.processDefinitionId -eq $process}
        $listDurationProcess = @()
        $info = "" | Select-Object $Columns
        foreach($instance in $processesInstances){
            $listDurationProcess += $instance.durationInMillis
        }
        if(![int]::IsNullOrEmpty -eq $listDurationProcess){
            $info.processDefinitionId = $instance.processDefinitionId
            $info.processDefinitionKey = $instance.processDefinitionKey
            $info.processDefinitionVersion = $instance.processDefinitionVersion
    
            $Measures = ($listDurationProcess | Measure-Object -Average -Maximum -Minimum)
            $info.minProcessDurationInMillis = $Measures.Minimum
            $info.meanProcessDurationInMillis = $Measures.Average
            $info.maxProcessDurationInMillis = $Measures.Maximum
            $info.countProcessInstance = $Measures.Count

            $csv += $info
        }
    }
    return $csv
}

function GetTaskIntancesMeasures($Columns){
    $csv = @()
    $data_Task = curl -XGET camunda:8080/engine-rest/history/task?processFinished=true | ConvertFrom-Json
    $listProcessDefinitionId = ($data_Task.processDefinitionId | Select-Object -Unique)
    foreach($processItem in $listProcessDefinitionId){
        $processIntances = $data_Task | Where-Object {$_.processDefinitionId -eq $processItem}
        $listTasks = ($processIntances.name | Select-Object -Unique)
        foreach($taskItem in $listTasks){
            $tasksIntances = $processIntances | Where-Object {$_.name -eq $taskItem}
            $listDurationTask = @()
            $info = "" | Select-Object $Columns
            foreach($task in $tasksIntances){
                $listDurationTask += $task.duration
            }
            if(![int]::IsNullOrEmpty -eq $listDurationTask){
                $info.processDefinitionId = $task.processDefinitionId
                $info.processDefinitionKey = $task.processDefinitionKey
                $info.processDefinitionVersion = $task.processDefinitionId.Split(":")[1]
                $info.taskName = $task.name
        
                $Measures = ($listDurationTask | Measure-Object -Average -Maximum -Minimum)
                $info.minTaskDurationInMillis = $Measures.Minimum
                $info.meanTaskDurationInMillis = $Measures.Average
                $info.maxTaskDurationInMillis = $Measures.Maximum
                $info.countTaskInstance = $Measures.Count
    
                $csv += $info
            }
        }
    }
    return $csv
}

function CreateDataJsonProcessIntances($csvImport){
    $csv = @()
    foreach ($row in $csvImport) {
        $index = Get-Content '.\json\indexPatten.json' | ConvertFrom-Json
        $index.update._id = $row.processDefinitionKey + "_" + $row.processDefinitionVersion
        $index.update._index = "processes"

        $csv+= $index

        $data = Get-Content '.\json\docPattenProcessInstance.json' | ConvertFrom-Json
        $data.doc.processDefinitionKey = $row.processDefinitionKey
        $data.doc.processDefinitionId = $row.processDefinitionId
        $data.doc.processDefinitionVersion = [int]$row.processDefinitionVersion
        $data.doc.processInstanceHistory.minProcessDurationInMillis = [int]$row.minProcessDurationInMillis
        $data.doc.processInstanceHistory.meanProcessDurationInMillis = [int]$row.meanProcessDurationInMillis
        $data.doc.processInstanceHistory.maxProcessDurationInMillis = [int]$row.maxProcessDurationInMillis
        $data.doc.processInstanceHistory.countProcessInstance = [int]$row.countProcessInstance
        
        $csv+= $data
    }
    $csv = $csv | Select-Object -Property * -ExcludeProperty id
    return $csv
}

function CreateDataJsonTask($csvImport){
    $csv = @()
    foreach ($row in $csvImport) {
        $index = Get-Content '.\json\indexPatten.json' | ConvertFrom-Json
        $index.update._id = $row.processDefinitionKey + "_" + $row.processDefinitionVersion
        $index.update._index = "processes"

        $csv+= $index

        $data = Get-Content '.\json\docPattenTask.json' | ConvertFrom-Json
        $data.doc.taskHistory.taskName.minTaskDurationInMillis = [int]$row.minTaskDurationInMillis
        $data.doc.taskHistory.taskName.meanTaskDurationInMillis = [int]$row.meanTaskDurationInMillis
        $data.doc.taskHistory.taskName.maxTaskDurationInMillis = [int]$row.maxTaskDurationInMillis
        $data.doc.taskHistory.taskName.countTaskInstance = [int]$row.countTaskInstance

        # Adding New property (Task to TaskHistory):
        $property = $data.doc.taskHistory.PSObject.Properties | Where-Object {$_.Name -eq "taskName"}
        # remember the current value of the old property
        $value = $property.Value
        # remove the "taskName" property
        $data.doc.taskHistory.PSObject.Properties.Remove($property.Name)
        # add the new property
        $data.doc.taskHistory | Add-Member -NotePropertyName $row.taskName -NotePropertyValue $value

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
        $bulk += $file.Substring(0,$index) + "`n"
        $file = $file.Substring($index + 1)
    }
    $bulk += $file
    $bulk | Out-File "bulk.json" # -Encoding utf8BOM
}


@(GetProcessIntancesMeasures -Columns $columnsProcess) | Select-Object $columnsProcess | Export-CSV -NoTypeInformation "./csv/ProcessIntancesMeasures.csv"
@(GetTaskIntancesMeasures -Columns $columnsTask) | Select-Object $columnsTask | Export-CSV -NoTypeInformation "./csv/TaskIntancesMeasures.csv"

$csvProcessIntancesMeasures = @(GetProcessIntancesMeasures -Columns $columnsProcess)
$csvTaskMeasures = @(GetTaskIntancesMeasures -Columns $columnsTask)

$json = @(CreateDataJsonProcessIntances -csvImport $csvProcessIntancesMeasures) + @(CreateDataJsonTask -csvImport $csvTaskMeasures) | ConvertTo-Json -Depth 100 -Compress

bulkJson -json $json
