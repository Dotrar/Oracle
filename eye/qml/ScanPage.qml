import QtQuick 2.11
import QtQuick.Controls 2.4

Page {
	property alias busyIndicator: busyIndicator

    header: Label {
        text: qsTr("Scanning..")
        font.pixelSize: Qt.application.font.pixelSize * 2
        padding: 10
    }
	BusyIndicator{
		id: busyIndicator
		anchors.fill: parent
	}
	Label{
		anchors.centerIn: parent
		text: qsTr("scanning part, please wait..")
	}
}
