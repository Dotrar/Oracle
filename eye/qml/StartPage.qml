import QtQuick 2.11
import QtQuick.Controls 2.4

Page {
	header: Label {
		text: qsTr("Oracle")
		font.pixelSize: Qt.application.font.pixelSize * 2
		padding: 10
	}
	Label{
		anchors.centerIn: parent
		text: qsTr("Swipe left to Scan")
	}
}
