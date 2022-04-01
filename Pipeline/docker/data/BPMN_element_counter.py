# It works with Python 3.8.6

import os
import lxml.etree
import glob
import csv
import sys

# Run with $python3 main.py path/to/bpmn/models/folder Output.csv
# First argument is the path to models folder
# Second argument is the output csv file name tha will be created in the script folder

with open(sys.argv[2],'w') as file:
    writer = csv.writer(file)
    #writer.writerow(["BPMN_File_Name","BPMN_Modeler","nTask","nTaskMultipleIstance","nTaskLoopActivity","nSendTask","nReceiveTask","nUserTask","nManualTask","nBusinessRuleTask","nServiceTask","nScriptTask","nCallActivity","nSubProcess","nTransaction","nAdHocSubProcess","nLane","nDataObject","nDataStore","nExclusiveGateway","nParallelGateway","nInclusiveGateway","nEventBasedGateway","nComplexGateway","nCondition","nStartMultipleParallelEventDefinition","nStartMultipleEventDefinition","nStartNoneEvent","nStartSignalEventDefinition","nStartConditionalEventDefinition","nStartTimerEventDefinition","nStartMessageEventDefinition","nStartCompensateEventDefinition","nStartCancelEventDefinition","nStartEscalationEventDefinition","nStartErrorEventDefinition","nEndEventNone","nEndTerminateEventDefinition","nEndEscalationEventDefinition","nEndMessageEventDefinition","nEndErrorEventDefinition","nEndCompensateEventDefinition","nEndCancelEventDefinition","nEndSignalEventDefinition","nEndMultipleEventDefinition","nIntermediateCatchMultipleEventDefinition","nIntermediateCatchMultipleParallelEventDefinition","nIntermediateCatchMessageEventDefinition","nIntermediateCatchTimerEventDefinition","nIntermediateCatchConditionalEventDefinition","nIntermediateCatchLinkEventDefinition","nIntermediateCatchSignalEventDefinition","nIntermediateThrowNoneEvent","nIntermediateThrowMessageEventDefinition","nIntermediateThrowEscalationEventDefinition","nIntermediateThrowLinkEventDefinition","nIntermediateThrowSignalEventDefinition","nIntermediateThrowCompensateEventDefinition","nIntermediateThrowMultipleEventDefinition","nBoundaryMessageEvent","nBoundaryTimerEvent","nBoundaryCancelEvent","nBoundaryConditionalEvent","nBoundaryEscalationEvent","nBoundaryErrorEvent","nBoundarySignalEvent","nBoundaryCompensateEvent","nBoundaryTimerEventNonInt","nBoundaryEscalationEventNonInt","nBoundaryConditionalEventNonInt","nBoundaryMessageEventNonInt","nGroup","nMessageFlow","nSequenceFlow","nDefaultFlow","nConditionalFlow","nPool","nChoreographyTask","nChoreographyParticipant","nChoreographySubprocess","nAssociation","nTextAnnotation","nMessage","nConversation","nSubConversation","nCallConversation","nConversationLink","TotalRePrository","TotalElements"])
    writer.writerow(["FileName","BPMN_Modeler","nTask","nTaskMultipleIstance","nTaskLoopActivity","nSendTask","nReceiveTask","nUserTask","nManualTask","nBusinessRuleTask","nServiceTask","nScriptTask","nCollapsedSubProcess","nExpandedSubProcess","nAdHocSubProcess","nTransaction","nCallActivity","nExclusiveGateway","nParallelGateway","nInclusiveGateway","nEventBasedGateway","nComplexGateway","nStartNoneEvent","nStartMultipleParallelEventDefinition","nStartMultipleEventDefinition","nStartSignalEventDefinition","nStartConditionalEventDefinition","nStartTimerEventDefinition","nStartMessageEventDefinition","nStartCompensateEventDefinition","nStartCancelEventDefinition","nStartEscalationEventDefinition","nStartErrorEventDefinition","nIntermediateCatchMultipleEventDefinition","nIntermediateCatchMultipleParallelEventDefinition","nIntermediateCatchMessageEventDefinition","nIntermediateCatchTimerEventDefinition","nIntermediateCatchConditionalEventDefinition","nIntermediateCatchLinkEventDefinition","nIntermediateCatchSignalEventDefinition","nIntermediateThrowNoneEvent","nIntermediateThrowMessageEventDefinition","nIntermediateThrowEscalationEventDefinition","nIntermediateThrowLinkEventDefinition","nIntermediateThrowSignalEventDefinition","nIntermediateThrowCompensateEventDefinition","nIntermediateThrowMultipleEventDefinition","nBoundaryMessageEvent","nBoundaryTimerEvent","nBoundaryCancelEvent","nBoundaryConditionalEvent","nBoundaryEscalationEvent","nBoundaryErrorEvent","nBoundarySignalEvent","nBoundaryCompensateEvent","nBoundaryTimerEventNonInt","nBoundaryEscalationEventNonInt","nBoundaryConditionalEventNonInt","nBoundaryMessageEventNonInt","nEndEventNone","nEndTerminateEventDefinition","nEndEscalationEventDefinition","nEndMessageEventDefinition","nEndErrorEventDefinition","nEndCompensateEventDefinition","nEndCancelEventDefinition","nEndSignalEventDefinition","nEndMultipleEventDefinition","nSequenceFlow","nDefaultFlow","nConditionalFlow","nMessageFlow","nAssociation","nPool","nLane","nDataObject","nDataStore","nGroup","nTextAnnotation","nMessage","nChoreographyTask","nChoreographyParticipant","nChoreographySubprocess","nConversation","nSubConversation","nCallConversation","nConversationLink","TotalElements"])


numberOfInvalid=0

for files in os.listdir(sys.argv[1]):
    
    namespace = "bpmn:"

    fileName=0
    bpmnModeler=0
    nTask=0
    nTaskMultipleIstance=0
    nTaskLoopActivity=0
    nReceiveTask=0
    nSendTask=0
    nUserTask=0
    nManualTask=0
    nBusinessRuleTask=0
    nServiceTask=0
    nScriptTask=0
    nCallActivity=0
    nSubProcess=0
    nExpandedSubProcess=0
    nCollapsedSubProcess=0
    nTransaction=0
    nAdHocSubProcess=0
    nGroup=0
    nLane=0
    nDataObject=0
    nDataObjectReference=0
    nDataStore=0
    nDataStoreReference=0
    nDataInput=0
    nDataOutput=0
    nExclusiveGateway=0
    nParallelGateway=0
    nInclusiveGateway=0
    nEventBasedGateway=0
    nComplexGateway=0
    nCondition=0
    nStartMultipleParallelEventDefinition=0.0
    nStartMultipleEventDefinition=0.0
    nStartNoneEvent=0.0
    nStartSignalEventDefinition=0.0
    nStartConditionalEventDefinition=0.0
    nStartTimerEventDefinition=0.0
    nStartMessageEventDefinition=0.0
    nStartCompensateEventDefinition=0.0
    nStartCancelEventDefinition=0.0
    nStartEscalationEventDefinition=0.0
    nStartErrorEventDefinition=0.0
    nEndEventNone = 0.0
    nEndMultipleEventDefinition = 0.0 
    nEndEscalationEventDefinition= 0.0
    nEndErrorEventDefinition=  0.0
    nEndSignalEventDefinition=  0.0
    nEndCompensateEventDefinition=  0.0
    nEndCancelEventDefinition=  0.0 
    nEndMessageEventDefinition=  0.0
    nEndTerminateEventDefinition=  0.0
    nIntermediateCatchMultipleEventDefinition=0
    nIntermediateCatchMultipleParallelEventDefinition=0
    nIntermediateCatchMessageEventDefinition=0
    nIntermediateCatchTimerEventDefinition=0
    nIntermediateCatchConditionalEventDefinition=0
    nIntermediateCatchLinkEventDefinition=0
    nIntermediateCatchSignalEventDefinition=0
    nIntermediateThrowNoneEvent=0
    nIntermediateThrowMessageEventDefinition=0
    nIntermediateThrowEscalationEventDefinition=0
    nIntermediateThrowLinkEventDefinition=0
    nIntermediateThrowSignalEventDefinition=0
    nIntermediateThrowCompensateEventDefinition=0
    nIntermediateThrowMultipleEventDefinition=0
    nBoundaryMessageEvent=0
    nBoundaryTimerEvent=0
    nBoundaryCancelEvent=0
    nBoundaryConditionalEvent =0
    nBoundaryEscalationEvent=0
    nBoundaryErrorEvent=0
    nBoundarySignalEvent=0
    nBoundaryCompensateEvent=0
    nBoundaryTimerEventNonInt=0
    nBoundaryEscalationEventNonInt=0
    nBoundaryConditionalEventNonInt=0
    nBoundaryMessageEventNonInt=0
    nGroup=0
    nMessageFlow=0
    nSequenceFlow=0
    nDefaultFlow=0
    nConditionalFlow=0
    nPool=0
    nVerticalLane=0
    nVerticalPool=0
    nChoreographyTask=0
    nChoreographyParticipant=0
    nChoreographySubprocess=0
    nConversation=0
    nSubConversation=0
    nCallConversation=0
    nConversationLink=0
    nITSystem=0
    nAssociation=0
    nCompensateAssociation=0
    nUnidirectionalAssociation=0
    nUndirectedAssociation=0
    nBidirectionalAssociation=0
    nTextAnnotation=0
    ndataOutputAssociation=0
    ndataInputAssociation=0
    TotalElements=0

    str=""


    #print("Model Name "+files)
    if("bpmn" in files):
        
        try:
            doc = lxml.etree.parse(sys.argv[1]+'/'+files)
            str = open(sys.argv[1]+'/'+files,'r', encoding="utf8").read()
        except:
            numberOfInvalid=numberOfInvalid+1
            print(files)
            continue
            
        
        # Discover the modeler type
        if str.find('camunda') != -1:
            bpmnModeler = "Camunda"

        elif str.find('signavio') != -1:
            bpmnModeler = "Signavio"
            
        else: 
            bpmnModeler = "Undefined"
            
        # Setting the file name
        fileName = files
        
        #get document root
        root = doc.getroot()

        # Calcolo metriche dei file
        #######################################################
        # Task
        nTask=  (doc.xpath('count(//bpmn:task )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) - nTaskMultipleIstance - nTaskLoopActivity)
        # Consider isSequential="true" for the type of multiple istance
        nTaskMultipleIstance=  doc.xpath('count(//bpmn:task//bpmn:multiInstanceLoopCharacteristics )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nTaskLoopActivity=  doc.xpath('count(//bpmn:task//bpmn:standardLoopCharacteristics )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nSendTask=  doc.xpath('count(//bpmn:sendTask )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nReceiveTask=  doc.xpath('count(//bpmn:receiveTask )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nUserTask=  doc.xpath('count(//bpmn:userTask )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nManualTask=  doc.xpath('count(//bpmn:manualTask )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBusinessRuleTask=  doc.xpath('count(//bpmn:businessRuleTask )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nServiceTask=  doc.xpath('count(//bpmn:serviceTask )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nScriptTask=  doc.xpath('count(//bpmn:scriptTask )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nCallActivity=  doc.xpath('count(//bpmn:callActivity )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        nSubProcess=  doc.xpath('count(//bpmn:subProcess )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })

        expandedSubProcessShape= root.findall('.//bpmn:BPMNShape', namespaces={'bpmn': 'http://www.omg.org/spec/BPMN/20100524/DI'})
        # print(nExpandedSubProcessShape)

        subProcessList= root.findall('.//bpmn:subProcess', namespaces={'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'})
        #print(subProcessList)
        
        for sub in subProcessList :
            for expSub in expandedSubProcessShape :
                #print("id "+sub.get("id")+" bpmnElement "+expSub.get("bpmnElement")+"\n")
                if(sub.get("id")==expSub.get("bpmnElement")):
                    if(expSub.get("isExpanded")=="true"):
                        #print("Expanded Sub")
                        nExpandedSubProcess+=1

        #print(fileName)
        #print(nSubProcess)
        #print(nExpandedSubProcess)
        nCollapsedSubProcess=nSubProcess-nExpandedSubProcess
        #print(nCollapsedSubProcess)

        nEventSubProcess=  doc.xpath('count(//bpmn:subProcess[@triggeredByEvent="true"] )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nTransaction=  doc.xpath('count(//bpmn:transaction )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nAdHocSubProcess=  doc.xpath('count(//bpmn:adHocSubProcess )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        #######################################################
        # Message Flow   
        nMessageFlow= doc.xpath('count(//bpmn:messageFlow)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        # Default Flow
        nDefaultFlow= doc.xpath('count(//bpmn:exclusiveGateway[@default])', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        # Conditional Flow
        nConditionalFlow= doc.xpath('count(//bpmn:sequenceFlow//bpmn:conditionExpression)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        # Sequence Flow
        nSequenceFlow=  (doc.xpath('count(//bpmn:sequenceFlow)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) - nDefaultFlow - nConditionalFlow)
        #######################################################
        # Group
        nGroup=  doc.xpath('count(//bpmn:group )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        #######################################################
        # Pool/Participant
        nPool= doc.xpath('count(//bpmn:collaboration//bpmn:participant)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nLane=  doc.xpath('count(//bpmn:lane )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        nVerticalPool= doc.xpath('count(//bpmn:collaboration[@isHorizontal="false"])', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nVerticalLane= doc.xpath('count(//bpmn:lane[@isHorizontal="false"])', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        #######################################################
        # Data Object/Store
        nDataObject=  doc.xpath('count(//bpmn:dataObject )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nDataStore=  doc.xpath('count(//bpmn:dataStore )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nDataObjectReference=  doc.xpath('count(//bpmn:dataObjectReference )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nDataStoreReference=  doc.xpath('count(//bpmn:dataStoreReference )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nDataInput=  doc.xpath('count(//bpmn:dataInput )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nDataOutput=  doc.xpath('count(//bpmn:dataOutput )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        #######################################################
        # Gateway
        nExclusiveGateway=  doc.xpath('count(//bpmn:exclusiveGateway )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nParallelGateway=  doc.xpath('count(//bpmn:parallelGateway )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nInclusiveGateway=  doc.xpath('count(//bpmn:inclusiveGateway )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nEventBasedGateway=  doc.xpath('count(//bpmn:eventBasedGateway )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nComplexGateway= doc.xpath('count(//bpmn:complexGateway )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        #######################################################
        # Event - condition
        nCondition=  doc.xpath('count(//bpmn:condition )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        #######################################################
        # Event - Start

        all_start_event = root.findall('.//bpmn:startEvent', namespaces={'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'})
        
        for start_event in all_start_event:
            #Delete all extensionElements tags
            all_startEvents_except_extensionElements = list(start_event.getchildren())
            defCounter = 0.0
            #all_startEvents_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}extensionElements", start_event.getchildren()))
            #all_startEvents_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}outgoing", start_event.getchildren()))
            #all_startEvents_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}incoming", start_event.getchildren()))
            
            
            #Check if every endEvent tag have child xEndEventDefinition
            #if len(all_startEvents_except_extensionElements) == 1:
            #    nStartNoneEvent += 1

            #Check if every endEvent tag have child xEndEventDefinition
            #elif len(all_startEvents_except_extensionElements) > 2:
            #    nStartMultipleEventDefinition += 1
            #    continue
            
            
            #For each event in the array (that can present 1 or + elements) 
            for event_definition in all_startEvents_except_extensionElements:
                if event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}signalEventDefinition":
                    defCounter += 1
                    nStartSignalEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}conditionalEventDefinition":
                    defCounter += 1
                    nStartConditionalEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}timerEventDefinition":
                    defCounter += 1
                    nStartTimerEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}messageEventDefinition":
                    defCounter += 1
                    nStartMessageEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}compensateEventDefinition":
                    defCounter += 1
                    nStartCompensateEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}cancelEventDefinition":
                    defCounter += 1
                    nStartCancelEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}escalationEventDefinition":
                    defCounter += 1
                    nStartEscalationEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}errorEventDefinition":
                    defCounter += 1
                    nStartErrorEventDefinition += 1
                    
            if(defCounter>1):    
                if(start_event.get("parallelMultiple")=="true"):
                    nStartMultipleParallelEventDefinition += 1
                else:
                    nStartMultipleEventDefinition += 1
                
            if(defCounter==0):
                nStartNoneEvent +=1 
                

        #######################################################
        # Event - End
        #root = doc.getroot()
        all_end_event = root.findall('.//bpmn:endEvent', namespaces={'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'})
        
        for end_event in all_end_event:
            #Delete all extensionElements tags
            #all_events_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}extensionElements", end_event.getchildren()))
            all_events_except_extensionElements = list(end_event.getchildren())
            #all_events_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}incoming", end_event.getchildren()))
            #all_events_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}outgoing", end_event.getchildren()))
            
            #Check if every endEvent tag have child xEndEventDefinition
            #if len(all_events_except_extensionElements) == 1:
            #    nEndEventNone += 1

            #Check if every endEvent tag have child xEndEventDefinition
            #elif len(all_events_except_extensionElements) > 2:
            #   nEndMultipleEventDefinition += 1
            #    continue
            defCounter = 0.0
            
            #Per ogni evento contenuto nell'array (che può contenere 1 o più elementi) 
            for event_definition in all_events_except_extensionElements:
                if event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}terminateEventDefinition":
                    defCounter += 1
                    nEndTerminateEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}escalationEventDefinition":
                    defCounter += 1
                    nEndEscalationEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}errorEventDefinition":
                    defCounter += 1
                    nEndErrorEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}signalEventDefinition":
                    defCounter += 1
                    nEndSignalEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}compensateEventDefinition":
                    defCounter += 1
                    nEndCompensateEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}cancelEventDefinition":
                    defCounter += 1
                    nEndCancelEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}messageEventDefinition":
                    defCounter += 1
                    nEndMessageEventDefinition += 1
                    
            if(defCounter>1):    
                nEndMultipleEventDefinition += 1
                
            if(defCounter==0):
                nEndEventNone +=1
            
        #######################################################
        # Event - Intermediate Catch  
            
        # nIntermediateCatchMultipleEventDefinition=  doc.xpath('count(//bpmn:intermediateCatchEvent[@parallelMultiple="false"])', namespaces={
        # 'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        # })
        # nIntermediateCatchMultipleParallelEventDefinition=  doc.xpath('count(//bpmn:intermediateCatchEvent[@parallelMultiple="true"])', namespaces={
        # 'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        # })
        # nIntermediateCatchMessageEventDefinition=  doc.xpath('count(//bpmn:intermediateCatchEvent//bpmn:messageEventDefinition )', namespaces={
        # 'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        # })
        # nIntermediateCatchTimerEventDefinition=  doc.xpath('count(//bpmn:intermediateCatchEvent//bpmn:timerEventDefinition )', namespaces={
        # 'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        # })
        # nIntermediateCatchConditionalEventDefinition=  doc.xpath('count(//bpmn:intermediateCatchEvent//bpmn:conditionalEventDefinition )', namespaces={
        # 'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        # })
        # nIntermediateCatchLinkEventDefinition=  doc.xpath('count(//bpmn:intermediateCatchEvent//bpmn:linkEventDefinition )', namespaces={
        # 'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        # })
        # nIntermediateCatchSignalEventDefinition=  doc.xpath('count(//bpmn:intermediateCatchEvent//bpmn:signalEventDefinition )', namespaces={
        # 'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        # })

          #######################################################
        # Event - Intermediate Catch
        # Da sottrarre 
        
        #root = doc.getroot()
        all_intermediatecatch_event = root.findall('.//bpmn:intermediateCatchEvent', namespaces={'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'})
        
        for intermediatecatch_event in all_intermediatecatch_event:

            all_intermediatecatchevents_except_extensionElements = list(intermediatecatch_event.getchildren())

            defCounter = 0.0
            
            #Per ogni evento contenuto nell'array (che può contenere 1 o più elementi) 
            for event_definition in all_intermediatecatchevents_except_extensionElements:
                if event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}messageEventDefinition":
                    defCounter += 1
                    nIntermediateCatchMessageEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}timerEventDefinition":
                    defCounter += 1
                    nIntermediateCatchTimerEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}conditionalEventDefinition":
                    defCounter += 1
                    nIntermediateCatchConditionalEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}linkEventDefinition":
                    defCounter += 1
                    nIntermediateCatchLinkEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}signalEventDefinition":
                    defCounter += 1
                    nIntermediateCatchSignalEventDefinition += 1

            if(defCounter>1):    
                if(intermediatecatch_event.get("parallelMultiple")=="true"):
                    nIntermediateCatchMultipleParallelEventDefinition += 1
                else:
                    nIntermediateCatchMultipleEventDefinition += 1
  

        #######################################################
        # Event - Intermediate Throw
        # Da sottrarre 
        
        #root = doc.getroot()
        all_intermediatethrow_event = root.findall('.//bpmn:intermediateThrowEvent', namespaces={'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL'})
        
        for intermediatethrow_event in all_intermediatethrow_event:
            #Delete all extensionElements tags
            all_intermediatethrowevents_except_extensionElements = list(intermediatethrow_event.getchildren())
            #all_intermediatethrowevents_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}extensionElements", intermediatethrow_event.getchildren()))
            #all_intermediatethrowevents_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}incoming", intermediatethrow_event.getchildren()))
            #all_intermediatethrowevents_except_extensionElements = list(filter(lambda e : e.tag != f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}outgoing", intermediatethrow_event.getchildren()))

            #Check if every endEvent tag have child xEndEventDefinition
            #if len(all_intermediatethrowevents_except_extensionElements) == 1:
            #    nIntermediateThrowNoneEvent += 1

            #Check if every endEvent tag have child xEndEventDefinition
            #elif len(all_intermediatethrowevents_except_extensionElements) > 2:
            #    nIntermediateThrowMultipleEventDefinition += 1
            #   continue
            defCounter = 0.0
            
            #Per ogni evento contenuto nell'array (che può contenere 1 o più elementi) 
            for event_definition in all_intermediatethrowevents_except_extensionElements:
                if event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}linkEventDefinition":
                    defCounter += 1
                    nIntermediateThrowLinkEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}escalationEventDefinition":
                    defCounter += 1
                    nIntermediateThrowEscalationEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}signalEventDefinition":
                    defCounter += 1
                    nIntermediateThrowSignalEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}compensateEventDefinition":
                    defCounter += 1
                    nIntermediateThrowCompensateEventDefinition += 1
                elif event_definition.tag == f"{{{'http://www.omg.org/spec/BPMN/20100524/MODEL'}}}messageEventDefinition":
                    defCounter += 1
                    nIntermediateThrowMessageEventDefinition += 1
                    
            if(defCounter>1):    
                nIntermediateThrowMultipleEventDefinition += 1
                
            if(defCounter==0):
                nIntermediateThrowNoneEvent +=1
                
        #######################################################
        # Event - Boundary Non-Interrupting 
        nBoundaryTimerEventNonInt=  doc.xpath('count(//bpmn:boundaryEvent[@cancelActivity="false"]//bpmn:timerEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBoundaryEscalationEventNonInt=  doc.xpath('count(//bpmn:boundaryEvent[@cancelActivity="false"]//bpmn:escalationEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBoundaryConditionalEventNonInt=  doc.xpath('count(//bpmn:boundaryEvent[@cancelActivity="false"]//bpmn:conditionalEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBoundarySignalEventNonInt=  doc.xpath('count(//bpmn:boundaryEvent[@cancelActivity="false"]//bpmn:signalEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBoundaryMessageEventNonInt=  doc.xpath('count(//bpmn:boundaryEvent[@cancelActivity="false"]//bpmn:messageEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        ######################################################
        # Boundary Interrupting
        nBoundaryMessageEvent=  (doc.xpath('count(//bpmn:boundaryEvent//bpmn:messageEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) - nBoundaryMessageEventNonInt)
        nBoundaryTimerEvent=  (doc.xpath('count(//bpmn:boundaryEvent//bpmn:timerEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) - nBoundaryTimerEventNonInt)  
        nBoundaryConditionalEvent= (doc.xpath('count(//bpmn:boundaryEvent//bpmn:conditionalEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) - nBoundaryConditionalEventNonInt)
        nBoundaryEscalationEvent=  (doc.xpath('count(//bpmn:boundaryEvent//bpmn:escalationEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) - nBoundaryEscalationEventNonInt)
        nBoundarySignalEvent= (doc.xpath('count(//bpmn:boundaryEvent//bpmn:signalEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) - nBoundarySignalEventNonInt)
        nBoundaryCancelEvent=  doc.xpath('count(//bpmn:boundaryEvent//bpmn:cancelEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBoundaryErrorEvent=  doc.xpath('count(//bpmn:boundaryEvent//bpmn:errorEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBoundaryCompensateEvent=  doc.xpath('count(//bpmn:boundaryEvent//bpmn:compensateEventDefinition)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        #######################################################
        # Choreography
        nChoreographyParticipant= doc.xpath('count(//bpmn:choreography//bpmn:participant )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nChoreographyTask= doc.xpath('count(//bpmn:choreographyTask)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nChoreographySubprocess= doc.xpath('count(//bpmn:subChoreography)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        #######################################################
        # Conversation
        nConversation= doc.xpath('count(//bpmn:conversation)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nSubConversation= doc.xpath('count(//bpmn:subConversation)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nCallConversation= doc.xpath('count(//bpmn:callConversation)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nConversationLink= doc.xpath('count(//bpmn:conversationLink)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        #######################################################
        # Message
        nMessage= doc.xpath('count(//bpmn:message)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        #######################################################
        # ITSystem not implemented
        nITSystem= doc.xpath('count(//bpmn:textAnnotation//bpmn:extensionElements[@dataObjectType="IT-systems"])', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        #######################################################
        # TextAnnotation
        nTextAnnotation= doc.xpath('count(//bpmn:textAnnotation)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        #######################################################
        # Association 
        ndataInputAssociation= doc.xpath('count(//bpmn:dataInputAssociation)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        ndataOutputAssociation= doc.xpath('count(//bpmn:dataOutputAssociation)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nAssociation= (doc.xpath('count(//bpmn:association)', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        }) + ndataInputAssociation + ndataOutputAssociation)  
        nCompensateAssociation= doc.xpath('count(//bpmn:endEvent//bpmn:compensateEventDefinition[@waitForCompletion="true"] )', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nUnidirectionalAssociation= doc.xpath('count(//bpmn:association[@associationDirection="One"])', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nUndirectedAssociation= doc.xpath('count(//bpmn:association[@associationDirection="None"])', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        nBidirectionalAssociation = doc.xpath('count(//bpmn:association[@associationDirection="Both"])', namespaces={
        'bpmn': 'http://www.omg.org/spec/BPMN/20100524/MODEL',
        })
        
        #######################################################
        # # Write Output
        
        #TotalElements=nTask+nTaskMultipleIstance+nTaskLoopActivity+nSendTask+nReceiveTask+nUserTask+nManualTask+nBusinessRuleTask+nServiceTask+nScriptTask+nCallActivity+nSubProcess+nTransaction+nAdHocSubProcess+nLane+nDataObject+nDataStore+nExclusiveGateway+nParallelGateway+nInclusiveGateway+nEventBasedGateway+nComplexGateway+nCondition+nStartMultipleParallelEventDefinition+nStartMultipleEventDefinition+nStartNoneEvent+nStartSignalEventDefinition+nStartConditionalEventDefinition+nStartTimerEventDefinition+nStartMessageEventDefinition+nStartCompensateEventDefinition+nStartCancelEventDefinition+nStartEscalationEventDefinition+nStartErrorEventDefinition+nEndEventNone+nEndTerminateEventDefinition+nEndEscalationEventDefinition+nEndMessageEventDefinition+nEndErrorEventDefinition+nEndCompensateEventDefinition+nEndCancelEventDefinition+nEndSignalEventDefinition+nEndMultipleEventDefinition+nIntermediateCatchMultipleEventDefinition+nIntermediateCatchMultipleParallelEventDefinition+nIntermediateCatchMessageEventDefinition+nIntermediateCatchTimerEventDefinition+nIntermediateCatchConditionalEventDefinition+nIntermediateCatchLinkEventDefinition+nIntermediateCatchSignalEventDefinition+nIntermediateThrowNoneEvent+nIntermediateThrowMessageEventDefinition+nIntermediateThrowEscalationEventDefinition+nIntermediateThrowLinkEventDefinition+nIntermediateThrowSignalEventDefinition+nIntermediateThrowCompensateEventDefinition+nIntermediateThrowMultipleEventDefinition                       +nBoundaryMessageEvent+nBoundaryTimerEvent+nBoundaryCancelEvent+nBoundaryConditionalEvent +nBoundaryEscalationEvent+nBoundaryErrorEvent+nBoundarySignalEvent+nBoundaryCompensateEvent+nBoundaryTimerEventNonInt+nBoundaryEscalationEventNonInt+nBoundaryConditionalEventNonInt+nBoundaryMessageEventNonInt+nGroup+nMessageFlow+nSequenceFlow+nDefaultFlow+nConditionalFlow+nPool+nChoreographyTask+nChoreographyParticipant+nChoreographySubprocess+nAssociation+nTextAnnotation+nMessage+nConversation+nSubConversation+nCallConversation+nConversationLink
        TotalElements=nTask+nTaskMultipleIstance+nTaskLoopActivity+nSendTask+nReceiveTask+nUserTask+nManualTask+nBusinessRuleTask+nServiceTask+nScriptTask+nCollapsedSubProcess+nExpandedSubProcess+nAdHocSubProcess+nTransaction+nCallActivity+nExclusiveGateway+nParallelGateway+nInclusiveGateway+nEventBasedGateway+nComplexGateway+nStartNoneEvent+nStartMultipleParallelEventDefinition+nStartMultipleEventDefinition+nStartSignalEventDefinition+nStartConditionalEventDefinition+nStartTimerEventDefinition+nStartMessageEventDefinition+nStartCompensateEventDefinition+nStartCancelEventDefinition+nStartEscalationEventDefinition+nStartErrorEventDefinition+nIntermediateCatchMultipleEventDefinition+nIntermediateCatchMultipleParallelEventDefinition+nIntermediateCatchMessageEventDefinition+nIntermediateCatchTimerEventDefinition+nIntermediateCatchConditionalEventDefinition+nIntermediateCatchLinkEventDefinition+nIntermediateCatchSignalEventDefinition+nIntermediateThrowNoneEvent+nIntermediateThrowMessageEventDefinition+nIntermediateThrowEscalationEventDefinition+nIntermediateThrowLinkEventDefinition+nIntermediateThrowSignalEventDefinition+nIntermediateThrowCompensateEventDefinition+nIntermediateThrowMultipleEventDefinition+nBoundaryMessageEvent+nBoundaryTimerEvent+nBoundaryCancelEvent+nBoundaryConditionalEvent+nBoundaryEscalationEvent+nBoundaryErrorEvent+nBoundarySignalEvent+nBoundaryCompensateEvent+nBoundaryTimerEventNonInt+nBoundaryEscalationEventNonInt+nBoundaryConditionalEventNonInt+nBoundaryMessageEventNonInt+nEndEventNone+nEndTerminateEventDefinition+nEndEscalationEventDefinition+nEndMessageEventDefinition+nEndErrorEventDefinition+nEndCompensateEventDefinition+nEndCancelEventDefinition+nEndSignalEventDefinition+nEndMultipleEventDefinition+nSequenceFlow+nDefaultFlow+nConditionalFlow+nMessageFlow+nAssociation+nPool+nLane+nDataObject+nDataStore+nGroup+nTextAnnotation+nMessage+nChoreographyTask+nChoreographyParticipant+nChoreographySubprocess+nConversation+nSubConversation+nCallConversation+nConversationLink+TotalElements

        TotalRePrository= ndataInputAssociation + ndataOutputAssociation+ (TotalElements - (nPool+nLane+nMessageFlow+nTextAnnotation+nAssociation))
        
        with open(sys.argv[2],'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([fileName,bpmnModeler,int(nTask),int(nTaskMultipleIstance),int(nTaskLoopActivity),int(nSendTask),int(nReceiveTask),int(nUserTask),int(nManualTask),int(nBusinessRuleTask),int(nServiceTask),int(nScriptTask),int(nCollapsedSubProcess),int(nExpandedSubProcess),int(nAdHocSubProcess),int(nTransaction),int(nCallActivity),int(nExclusiveGateway),int(nParallelGateway),int(nInclusiveGateway),int(nEventBasedGateway),int(nComplexGateway),int(nStartNoneEvent),int(nStartMultipleParallelEventDefinition),int(nStartMultipleEventDefinition),int(nStartSignalEventDefinition),int(nStartConditionalEventDefinition),int(nStartTimerEventDefinition),int(nStartMessageEventDefinition),int(nStartCompensateEventDefinition),int(nStartCancelEventDefinition),int(nStartEscalationEventDefinition),int(nStartErrorEventDefinition),int(nIntermediateCatchMultipleEventDefinition),int(nIntermediateCatchMultipleParallelEventDefinition),int(nIntermediateCatchMessageEventDefinition),int(nIntermediateCatchTimerEventDefinition),int(nIntermediateCatchConditionalEventDefinition),int(nIntermediateCatchLinkEventDefinition),int(nIntermediateCatchSignalEventDefinition),int(nIntermediateThrowNoneEvent),int(nIntermediateThrowMessageEventDefinition),int(nIntermediateThrowEscalationEventDefinition),int(nIntermediateThrowLinkEventDefinition),int(nIntermediateThrowSignalEventDefinition),int(nIntermediateThrowCompensateEventDefinition),int(nIntermediateThrowMultipleEventDefinition),int(nBoundaryMessageEvent),int(nBoundaryTimerEvent),int(nBoundaryCancelEvent),int(nBoundaryConditionalEvent),int(nBoundaryEscalationEvent),int(nBoundaryErrorEvent),int(nBoundarySignalEvent),int(nBoundaryCompensateEvent),int(nBoundaryTimerEventNonInt),int(nBoundaryEscalationEventNonInt),int(nBoundaryConditionalEventNonInt),int(nBoundaryMessageEventNonInt),int(nEndEventNone),int(nEndTerminateEventDefinition),int(nEndEscalationEventDefinition),int(nEndMessageEventDefinition),int(nEndErrorEventDefinition),int(nEndCompensateEventDefinition),int(nEndCancelEventDefinition),int(nEndSignalEventDefinition),int(nEndMultipleEventDefinition),int(nSequenceFlow),int(nDefaultFlow),int(nConditionalFlow),int(nMessageFlow),int(nAssociation),int(nPool),int(nLane),int(nDataObject),int(nDataStore),int(nGroup),int(nTextAnnotation),int(nMessage),int(nChoreographyTask),int(nChoreographyParticipant),int(nChoreographySubprocess),int(nConversation),int(nSubConversation),int(nCallConversation),int(nConversationLink),int(TotalElements)])
            # writer.writerow([fileName,bpmnModeler,nTask,nTaskMultipleIstance,nTaskLoopActivity,nSendTask,nReceiveTask,nUserTask,nManualTask,nBusinessRuleTask,nServiceTask,nScriptTask,nCallActivity
            #             ,nSubProcess,nCollapsedSubProcess,nExpandedSubProcess,nTransaction,nAdHocSubProcess
            #             ,nLane,nDataObject,nDataStore                       
            #             ,nExclusiveGateway,nParallelGateway,nInclusiveGateway,nEventBasedGateway,nComplexGateway,nCondition
            #             ,nStartMultipleParallelEventDefinition,nStartMultipleEventDefinition,nStartNoneEvent,nStartSignalEventDefinition,nStartConditionalEventDefinition
            #             ,nStartTimerEventDefinition,nStartMessageEventDefinition,nStartCompensateEventDefinition,nStartCancelEventDefinition
            #             ,nStartEscalationEventDefinition,nStartErrorEventDefinition,nEndEventNone,nEndTerminateEventDefinition,nEndEscalationEventDefinition
            #             ,nEndMessageEventDefinition,nEndErrorEventDefinition,nEndCompensateEventDefinition
            #             ,nEndCancelEventDefinition,nEndSignalEventDefinition,nEndMultipleEventDefinition,nIntermediateCatchMultipleEventDefinition,nIntermediateCatchMultipleParallelEventDefinition,nIntermediateCatchMessageEventDefinition
            #             ,nIntermediateCatchTimerEventDefinition,nIntermediateCatchConditionalEventDefinition,nIntermediateCatchLinkEventDefinition
            #             ,nIntermediateCatchSignalEventDefinition,nIntermediateThrowNoneEvent,nIntermediateThrowMessageEventDefinition
            #             ,nIntermediateThrowEscalationEventDefinition,nIntermediateThrowLinkEventDefinition
            #             ,nIntermediateThrowSignalEventDefinition,nIntermediateThrowCompensateEventDefinition,nIntermediateThrowMultipleEventDefinition                       
            #             ,nBoundaryMessageEvent,nBoundaryTimerEvent
            #             ,nBoundaryCancelEvent,nBoundaryConditionalEvent ,nBoundaryEscalationEvent
            #             ,nBoundaryErrorEvent,nBoundarySignalEvent,nBoundaryCompensateEvent
            #             ,nBoundaryTimerEventNonInt,nBoundaryEscalationEventNonInt,nBoundaryConditionalEventNonInt
            #             ,nBoundaryMessageEventNonInt,nGroup,nMessageFlow,nSequenceFlow,nDefaultFlow,nConditionalFlow,nPool,
            #             nChoreographyTask,nChoreographyParticipant,nChoreographySubprocess,nAssociation,nTextAnnotation,nMessage,nConversation,nSubConversation,nCallConversation,nConversationLink,TotalRePrository,TotalElements])
        #print("Elements of "+fileName+" file with: "+bpmnModeler+" are succesfully counted ")
    # Convert the dataframe to an XlsxWriter Excel object e quindi aggiungo la riga nel file excel
    #df.to_csv('BPMN-metrics-output.csv', header=1, index=False, mode = 'a')

