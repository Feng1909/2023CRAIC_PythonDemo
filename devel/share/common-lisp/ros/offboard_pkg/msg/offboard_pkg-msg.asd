
(cl:in-package :asdf)

(defsystem "offboard_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ArucoInfo" :depends-on ("_package_ArucoInfo"))
    (:file "_package_ArucoInfo" :depends-on ("_package"))
    (:file "Message" :depends-on ("_package_Message"))
    (:file "_package_Message" :depends-on ("_package"))
    (:file "MultiArucoInfo" :depends-on ("_package_MultiArucoInfo"))
    (:file "_package_MultiArucoInfo" :depends-on ("_package"))
  ))