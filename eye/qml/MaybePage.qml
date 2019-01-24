import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11
import QtQuick.Controls.Styles 1.4
import Oracle 1.0

Page {
	id: maybePage
	
	Keys.onReturnPressed: if(this.StackView.view) this.StackView.view.pop()	//keyboard delete for debugging

	SwipeView{
		id: possibilitiesSwipe
		anchors.fill: parent
		onCurrentItemChanged:{
			if(currentItem)
			{console.log(currentItem.code)}
		}
		Repeater {
			model: oracle.response
			delegate: ProductItem {
				code: modelData
			}
		}
	}
	PageIndicator {
		id: indicator
		count: possibilitiesSwipe.count
		currentIndex: possibilitiesSwipe.currentIndex
		anchors.bottom: parent.bottom
		anchors.horizontalCenter: parent.horizontalCenter
	}
	footer: DialogButtonBox {
		alignment: undefined

		Button {
			text: qsTr("Save")
			DialogButtonBox.buttonRole: DialogButtonBox.AcceptRole
		}
		Button {
			text: qsTr("Close")
			DialogButtonBox.buttonRole: DialogButtonBox.DestructiveRole
		}
	}
  /* 
	RowLayout{
		id: footer
		DelayButton{
			id: noneButton
			Layout.fillWidth: true
			Layout.fillHeight: true
			text: 'None of these'
			onActivated: maybePage.StackView.view.replace(Qt.resolvedUrl("UnsurePage.qml"))
		}
		DelayButton{
			id: confirmButton
			Layout.fillWidth: true
			Layout.fillHeight: true
			text: possibilitiesSwipe.currentItem.code
			onActivated: {
				oracle.select(possibilitiesSwipe.currentItem.code)
			}
		}
	}*/


}
