import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11
import QtQuick.Controls.Styles 1.4
import Oracle 1.0

Page {
	id: maybePage
	//width: parent.width
	//height: parent.height
	header: Label {
		id: header
		//text: qsTr("It might be one of these...")
		text: possibilitiesSwipe.currentItem.code
		anchors.horizontalCenter: parent.horizontalCenter
		horizontalAlignment: Text.AlignHCenter
		font.pixelSize: Qt.application.font.pixelSize * 2
		padding: 10
	}
	Keys.onReturnPressed: if(this.StackView.view) this.StackView.view.pop()	//keyboard delete for debugging


	PageIndicator {
		id: indicator
		count: possibilitiesSwipe.count
		currentIndex: possibilitiesSwipe.currentIndex
		anchors.bottom: parent.bottom
		anchors.horizontalCenter: parent.horizontalCenter
	}

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
	footer:RowLayout{
		spacing: 0
		height: 80		//on 5" screen this is only 10% of screen
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
	}


}
