import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Window 2.2
import QtQuick.Controls.Material 2.4

Window {
	id: window
	visible: true
	width: 480
	height: 800
	title: qsTr("Oracle")


	StackView {
		id: pagesStack
		property ProductItem selectedItem : null
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
				focus: true
				busyIndicator.running: this.focus
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

 }
