import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QTextEdit, QComboBox,
    QPushButton, QFormLayout, QMessageBox, QShortcut, QLabel, QVBoxLayout
)
from PyQt5.QtGui import QKeySequence

class FormValidationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        form_layout.addRow("Name:", self.name_input)

        self.email_input = QLineEdit()
        form_layout.addRow("Email:", self.email_input)

        self.age_input = QLineEdit()
        form_layout.addRow("Age:", self.age_input)

        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62 000 0000 0000;_")
        form_layout.addRow("Phone Number:", self.phone_input)

        self.address_input = QTextEdit()
        form_layout.addRow("Address:", self.address_input)

        self.gender_input = QComboBox()
        self.gender_input.addItems(["", "Male", "Female"])
        form_layout.addRow("Gender:", self.gender_input)

        self.education_input = QComboBox()
        self.education_input.addItems(["", "Elementary School", "Junior High School",
                                       "Senior High School", "Diploma", "Bachelor's Degree",
                                       "Master's Degree", "Doctoral Degree"])
        form_layout.addRow("Education:", self.education_input)

      
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.validate_form)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)

        form_layout.addRow(self.save_button, self.clear_button)

        self.author_label = QLabel(" Andika Dhanan Jaya - F1D022111")  
        self.author_label.setStyleSheet("margin-top: 15px; font-weight: bold; color: black;")


        quit_shortcut = QShortcut(QKeySequence("Q"), self)
        quit_shortcut.activated.connect(self.close)

  
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.author_label)
        self.setLayout(main_layout)

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_input.currentText()
        education = self.education_input.currentText()

        # Validation rules
        if not all([name, email, age, phone, address, gender, education]):
            self.show_warning("All fields are required.")
            return

        if len(name) < 3:
            self.show_warning("Name must be at least 3 characters.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_warning("Invalid email format.")
            return

        if not age.isdigit():
            self.show_warning("Age must be numeric.")
            return

        if not (17 <= int(age) <= 100):
            self.show_warning("Age must be between 17 and 100.")
            return

        if not re.fullmatch(r"\+62 \d{3} \d{4} \d{4}", phone):
            self.show_warning("Phone number must follow +62 XXX XXXX XXXX format.")
            return

        QMessageBox.information(self, "Success", "Form submitted successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.education_input.setCurrentIndex(0)

    def show_warning(self, message):
        QMessageBox.warning(self, "Validation Error", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec_())
