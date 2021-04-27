import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Dialogs 1.3

Dialog {
    objectName: "loginDialog"
    id: loginDialog
    title: "Login to discord"
    standardButtons: Dialog.NoButton
    

    Page{
        Layout.fillWidth: true
        ColumnLayout {
            anchors.fill: parent
            spacing: 6

            TextField {
                id: email
                placeholderText: "Email"
                Layout.fillWidth: true
            }

            TextField {
                id: password
                placeholderText: "Password"
                echoMode: TextInput.Password
                Layout.fillWidth: true
            }

            RowLayout {
                Button {
                    text: "Login"
                    Layout.fillWidth: true
                }
                Button {
                    text: "Cancel"
                    onClicked: loginDialog.close()
                }
            }
        }
    }
}