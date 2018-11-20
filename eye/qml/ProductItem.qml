import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

Item {

	property alias code:  pLabel.text
	property alias img:  pImage.source

	ColumnLayout{
		Label {
			id: pLabel
			text: 'undefined'
		}
		Image {
			id: pImage
			source: 'base.jpg'
			fillMode: Image.Stretch
		}
	}
}
