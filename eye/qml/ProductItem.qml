import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11

Item {

	property alias code:  pLabel.text
	property alias img:  pImage.source

	RowLayout{
		Image {
			id: pImage
			source: 'base.jpg'
			fillMode: Image.PreserveAspectFit
		}
		Label {
			id: pLabel
			text: 'undefined'
		}
	}
}
//**** TODO
/*
	We need to adjust this to load dynamic content and have multiple properties and failsafes.

	such as when the product doesn't exsist

	as well as the blurb / pricing information

*/
