import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Dialogs 1.3

Dialog {

    // anchors.fill: parent

    ColumnLayout {
        anchors.fill: parent
        spacing: 6

        RowLayout {
            anchors.fill: parent
            spacing: 6

            Label {
                font.pixelSize: 22
                text: "Hejsan"
            }
        }

    }
    
}