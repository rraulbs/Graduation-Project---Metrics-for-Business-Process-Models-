<#

Raul Baptista de Souza
YYYY/MM/DD = 2022/03/17

.DESCRIPTION
This script is used for convert the output.csv file in a output.json file. Also prepare json with the correct Id.
--------------------------------------------------------
|Flag         | Description                            |
--------------------------------------------------------
|-Filename    | used to import the csv file            |
--------------------------------------------------------

* Convert the csv to json as shown in the example below.

.EXAMPLE
./UpdateDashboardKibana.ps1 -Filename "Output.csv"

.LINK
https://.../#documentation

#>

param(
    [Parameter(ParameterSetName="ParamSet", Mandatory=$true)][string] $FileName,
    [parameter(ParameterSetName="help", Mandatory=$true)][switch]$help, 
    [parameter(ParameterSetName="h", Mandatory=$true)][switch]$h
)

if(($PSCmdlet.ParameterSetName -eq 'help' -and $help) -or 
    ($PSCmdlet.ParameterSetName -eq 'h' -and $h)) {
    Get-Help $MyInvocation.MyCommand.Path -detailed
    exit
}

$InfoColumns = @("FileName","BPMN_Modeler")
$TotalColumn = @("TotalElements")
$ActivityTaskElements = @("nTask","nTaskMultipleIstance","nTaskLoopActivity","nSendTask","nReceiveTask","nUserTask","nManualTask","nBusinessRuleTask","nServiceTask","nScriptTask")
$ActivitySubprocessElements = @("nCollapsedSubProcess", "nExpandedSubProcess", "nAdHocSubProcess", "nTransaction", "nCallActivity")
$GatewayElements = @("nExclusiveGateway","nParallelGateway","nInclusiveGateway","nEventBasedGateway","nComplexGateway")
$EventStartElements = @("nStartNoneEvent","nStartMultipleParallelEventDefinition","nStartMultipleEventDefinition","nStartSignalEventDefinition","nStartConditionalEventDefinition","nStartTimerEventDefinition","nStartMessageEventDefinition","nStartCompensateEventDefinition","nStartCancelEventDefinition","nStartEscalationEventDefinition","nStartErrorEventDefinition")
$EventIntermediateCatchElements = @("nIntermediateCatchMultipleEventDefinition","nIntermediateCatchMultipleParallelEventDefinition","nIntermediateCatchMessageEventDefinition","nIntermediateCatchTimerEventDefinition","nIntermediateCatchConditionalEventDefinition","nIntermediateCatchLinkEventDefinition","nIntermediateCatchSignalEventDefinition")
$EventIntermediateThrowElements = @("nIntermediateThrowNoneEvent","nIntermediateThrowMessageEventDefinition","nIntermediateThrowEscalationEventDefinition","nIntermediateThrowLinkEventDefinition","nIntermediateThrowSignalEventDefinition","nIntermediateThrowCompensateEventDefinition","nIntermediateThrowMultipleEventDefinition")
$EventBoundaryElements = @("nBoundaryMessageEvent","nBoundaryTimerEvent","nBoundaryCancelEvent","nBoundaryConditionalEvent","nBoundaryEscalationEvent","nBoundaryErrorEvent","nBoundarySignalEvent","nBoundaryCompensateEvent","nBoundaryTimerEventNonInt","nBoundaryEscalationEventNonInt","nBoundaryConditionalEventNonInt","nBoundaryMessageEventNonInt")
$EventEndElements = @("nEndEventNone","nEndTerminateEventDefinition","nEndEscalationEventDefinition","nEndMessageEventDefinition","nEndErrorEventDefinition","nEndCompensateEventDefinition","nEndCancelEventDefinition","nEndSignalEventDefinition","nEndMultipleEventDefinition")
$ConnectingObjectsElements = @("nSequenceFlow","nDefaultFlow","nConditionalFlow","nMessageFlow","nAssociation")
$SwimlanesElements = @("nPool","nLane")
$ArtifactsElements = @("nDataObject","nDataStore","nGroup","nTextAnnotation","nMessage")
$ChoreographyElements = @("nChoreographyTask","nChoreographyParticipant","nChoreographySubprocess")
$ConversationElements = @("nConversation","nSubConversation","nCallConversation","nConversationLink")
$AllIntColumns = $TotalColumn + $ActivityTaskElements + $ActivitySubprocessElements + $GatewayElements + $EventStartElements + $EventIntermediateCatchElements + $EventIntermediateThrowElements + $EventBoundaryElements + $EventEndElements + $ConnectingObjectsElements + $SwimlanesElements + $ArtifactsElements + $ChoreographyElements + $ConversationElements

function CreateDataJson($csvImport){
    $csv = @()
    foreach ($row in $csvImport) {        
        $id = $row.FileName
        $id = $($row.FileName).split('.')[0]
        # $id = $id.Split('_')[-1]
        $index = Get-Content '.\indexPatten.json' | ConvertFrom-Json
        $index.index._id = $id
        $csv+= $index
        $data = $row
        foreach($column in $AllIntColumns){
            $data.$column = [int]$data.$column
        }
        $csv+= $data
    }
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

if(![string]::IsNullOrEmpty($FileName)) {
    $csv = Import-Csv -Path "./$($FileName)" -Delimiter ","
    # $date = [string]::format("{0:yyyy-MM-dd}", [DateTime]::now)
    $json = @(CreateDataJson -csvImport $csv) | ConvertTo-Json -Depth 100 -Compress
    bulkJson -jsonImport -json $json
} else {
    throw 'FileName parameter must be provide.'
}
