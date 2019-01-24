import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Window 2.2
import QtQuick.Controls.Material 2.4
import Oracle 1.0

Window {
	id: window
	visible: true
	height: 480
	width: 800
	title: qsTr("Oracle")

	Oracle{
		id: oracle
		onResponseReceived: {
			console.log("response received")
			var len = response.length;
			if(len == 1){
				this.selection = response[0] //triggers selection changed
			}

			if(len > 1 && len < 5){	//push swipe page for possible options
				pagesStack.push(Qt.resolvedUrl("MaybePage.qml"))
			} else {				//unsure completely
				pagesStack.push(Qt.resolvedUrl("UnsurePage.qml"))
			}
		}
		onSelectionChanged: {
			pagesStack.push(Qt.resolvedUrl("SurePage.qml"))
		}
	}

	StackView {
		id: pagesStack
		anchors.fill: parent
		focus: true
		onCurrentItemChanged: {
			if (currentItem) {
				currentItem.forceActiveFocus()
			}
		}

		Keys.onReturnPressed: console.log("return in stack")


		initialItem: SwipeView {
			id: swipeView							//swipeview has both the start and scan pages
			focus: true
			onCurrentItemChanged: {
				if (currentItem) {
					currentItem.forceActiveFocus()
				}
			}

			StartPage {
				id: startPage
			}

			ScanPage {
				id: scanPage
				busyIndicator.running: this.focus
				states: [
					State{
						name: "scanningState"
						when: scanPage.focus
						StateChangeScript{
							name: "runScan"
							script:{
								oracle.capture()
							}
						}
					},
					State{
						name: "idle"
						when: !scanPage.focus
						StateChangeScript{
							name: "cancelScan"
							script:{
								console.log("CANCEL")
								oracle.cancel()
							}
						}
					}
				]
				//debugginc controls, ideally remove this but can keep it for debuggin
				 Keys.onPressed: {
					 if (event.key == Qt.Key_1) 		pagesStack.push(Qt.resolvedUrl("UnsurePage.qml"))
					 else if (event.key == Qt.Key_2) pagesStack.push(Qt.resolvedUrl("MaybePage.qml"))
					 else if (event.key == Qt.Key_3) pagesStack.push(Qt.resolvedUrl("SurePage.qml"))
					 else 							console.log(event.key)
				 }




			 }
		 }

		 pushEnter: Transition {
			 PropertyAnimation {
				 property: "opacity"
				 from: 0
				 to:1
				 duration: 200
			 }
		 }
		 pushExit: Transition {
			 PropertyAnimation {
				 property: "opacity"
				 from: 1
				 to:0
				 duration: 200
			 }
		 }
		 popEnter: Transition {
			 PropertyAnimation {
				 property: "opacity"
				 from: 0
				 to:1
				 duration: 200
			 }
		 }
		 popExit: Transition {
			 PropertyAnimation {
				 property: "opacity"
				 from: 1
				 to:0
				 duration: 200
			 }
		 }


	 }
 }


 /*
  InputPanel {
	  id: inputPanel
	  z: 99
	  x: 0
	  y: window.height
	  width: window.width

	  states: State {
		  name: "visible"
		  when: inputPanel.active
		  PropertyChanges {
			  target: inputPanel
			  y: window.height - inputPanel.height
		  }
	  }
	  transitions: Transition {
		  from: ""
		  to: "visible"
		  reversible: true
		  ParallelAnimation {
			  NumberAnimation {
				  properties: "y"
				  duration: 250
				  easing.type: Easing.InOutQuad
			  }
		  }
	  }
  }*/
