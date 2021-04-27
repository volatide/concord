import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls 2.15
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.15
import QtQuick.Window 2.15
import '.'

Page {
    anchors.fill: parent
    id: concord

    RowLayout {
        spacing: 0
        anchors.fill: parent

        ColumnLayout {
            id: serverList
            Layout.maximumWidth: 72

            Rectangle {
                width: parent.width
                height: parent.height
                color: "steelblue"
            }

        }

        ColumnLayout {
            id: channelList
            Layout.maximumWidth: 240

            Rectangle {
                width: parent.width
                height: parent.height
                color: "red"
            }

        }

        ColumnLayout {
            id: contentList

            Rectangle {
                width: parent.width
                height: parent.height
                color: "yellow"
            }

        }

    }

    LoginDialog {
        id: login_dialog
    }

}
