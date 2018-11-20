import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

Page {
	id: surePage
	width: parent.width
	height: parent.height
	property ProductItem item: parent.selectedItem

	header: Label {
		text: item.code
		font.pixelSize: Qt.application.font.pixelSize * 2
		horizontalAlignment: Text.AlignHCenter
		padding: 10
	}
	ColumnLayout{
		anchors.fill: parent
		Image {
			Layout.preferredHeight: 400
			fillMode: Image.PreserveAspectFit
			source: item.img
		}
		Label{
			Layout.fillHeight: true
			Layout.margins: 10
			text: 'A water type pokemon'
		}

	}
	Keys.onReturnPressed: if(this.StackView.view) this.StackView.view.pop()
	footer:RowLayout{
		spacing: 0
		height: 80		//on 5" screen this is only 10% of screen
		DelayButton{
			id: noneButton
			Layout.fillWidth: true
			Layout.fillHeight: true
			text: "Mine seems different"
			onActivated: surePage.StackView.view.replace(Qt.resolvedUrl("UnsurePage.qml"))	
		}
		DelayButton{
			id: confirmButton
			Layout.fillWidth: true
			Layout.fillHeight: true
			text: "Yep, that's the one"
			onActivated: {
				swipeView.currentIndex = 0
				surePage.StackView.view.pop()
			}
		}
	}
}
