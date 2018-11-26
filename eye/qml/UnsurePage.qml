import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11
import OracleKeypad 1.0

Page {
	id: unsurePage
	width: parent.width
	height: parent.height
	header: Label {
		text: qsTr("Unsure")
		font.pixelSize: Qt.application.font.pixelSize * 2
		padding: 10
	}

	// for debugging
	Keys.onReturnPressed: if(this.StackView.view) this.StackView.view.pop()

	OracleKeypad {
		id: keypad
		onKeypadChanged: console.log('keypadchanged')
		onFinished: {
			oracle.select(keypad.value)
			unsurePage.StackView.view.replace(Qt.resolvedUrl("SurePage.qml"))
		}
	}

	ColumnLayout{
		anchors.fill: parent
		Label {
			text: qsTr("Please find manually and input below:")
		}
		RowLayout{
			Text{
				id:input
				text: keypad.value
				font.pixelSize: Qt.application.font.pixelSize *1.5
				padding: 10
				Layout.fillWidth: true
			}
			Button {
				text: '<<'
				onPressed: keypad.backspace()
			}
		}
		GridLayout{
			Layout.fillWidth: true
			Layout.fillHeight: true
			columns: 3
			Repeater{
				model: keypad.model
				delegate:Button{
					Layout.fillWidth: true
					Layout.fillHeight: true
					text: modelData
					font.pixelSize: Qt.application.font.pixelSize * 2
					onPressed: keypad.pressed(modelData)
				}
			}
		}
	}

}

