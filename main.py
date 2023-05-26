import sys
from PyQt5 import QtWidgets
from login import Ui_Login
from main_window import Ui_MainWindow
from sign_in import Ui_SignIn
from stats import Ui_Stats
from reports_backlog import Ui_ReportsWindow
from new_task import Ui_NewTask
from task import Ui_TaskWindow
from new_project import Ui_NewProject
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import psycopg2
import datetime


# Connect to database
con = psycopg2.connect(
    database="kp0092_17_2",
    user="st0092",
    password="qwerty92",
    host="172.20.8.18",
    port="5432"
)
cur = con.cursor()

# cur.execute("SELECT * FROM users")
# print(cur.fetchall())


class login(QtWidgets.QDialog, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_button.clicked.connect(self.open_main_win)
        self.create_acc_button.clicked.connect(self.open_sign_in)

    def open_main_win(self):
        self.login = self.login_input.text()
        self.password = self.pass_input.text()

        cur.execute("SELECT id, role FROM users WHERE login = %s AND password = %s", (self.login, self.password))
        code_and_role = cur.fetchall()
        print(code_and_role)

        if code_and_role != []:
            self.id = code_and_role[0][0]
            self.role = code_and_role[0][1]
            self.main_win = main_win(self.role, self.id)
            self.main_win.show()
            self.close()
        else:
            self.login_input.setStyleSheet("border: 1px;\n"
            "border-color: rgb(255, 0, 0);\n"
            "border-style: outset;\n"
            "border-radius: 8px;")
            self.pass_input.setStyleSheet("border: 1px;\n"
            "border-color: rgb(255, 0, 0);\n"
            "border-style: outset;\n"
            "border-radius: 8px;")
            # error message
            print('error')

    def open_sign_in(self):
        self.sign_in = sign_in()
        self.sign_in.show()
        self.close()

class main_win(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, role, id):
        super().__init__()
        self.role = role
        self.id = id
        self.setupUi(self)
        self.stats_button.clicked.connect(self.open_stats)
        self.refresh_button.clicked.connect(self.refresh)
        self.reports_button.clicked.connect(self.open_reports)
        self.backlog_button.clicked.connect(self.open_backlog)
        if self.role != 'admin':
            self.new_project_button.hide()
            self.new_task_button.hide()
        self.new_project_button.clicked.connect(self.open_new_project)
        self.new_task_button.clicked.connect(self.open_new_task)

        # query for names of projects to combobox where code of user is in codes_users column in projects table in charvar format like '1, 2, 3, 11, 12, 111, 112'
        cur.execute("SELECT name FROM projects WHERE codes_users LIKE %s", ('%' + str(self.id) + '%',))
        self.projects = cur.fetchall()
        for project in self.projects:
            self.projectname_combo_box.addItem(project[0])

        self.projectname_combo_box.currentTextChanged.connect(self.refresh_lists)
        self.todo_list.clear()
        self.in_progress_list.clear()
        self.done_list.clear()
        
        # query for tasks of project
        self.project_name = self.projectname_combo_box.currentText()
        cur.execute("SELECT projects.id FROM projects left join tasks on projects.id = tasks.project_id WHERE projects.name = %s", (self.project_name,))
        id_projects = cur.fetchall()
        print(id_projects)

        if id_projects not in [[], None]:
            self.id_project = id_projects[0][0]
        else:
            self.id_project = None
            self.projectname_combo_box.clear()

        cur.execute("SELECT id, name, status FROM tasks WHERE project_id = %s AND status = 'todo' and empl_code = %s", (self.id_project, self.id))
        self.todo_tasks = cur.fetchall()
        print(self.todo_tasks)
        for task in self.todo_tasks:
            self.todo_list.addItem(str(task[0]) + ' \n ' + str(task[1]))
        cur.execute("SELECT id, name, status FROM tasks WHERE project_id = %s AND status = 'in progress' and empl_code = %s", (self.id_project, self.id))
        self.in_progress_tasks = cur.fetchall()
        for task in self.in_progress_tasks:
            self.in_progress_list.addItem(str(task[0]) + ' \n ' + str(task[1]))
        cur.execute("SELECT id, name, status FROM tasks WHERE project_id = %s AND status = 'done' and empl_code = %s", (self.id_project, self.id))
        self.done_tasks = cur.fetchall()
        for task in self.done_tasks:
            self.done_list.addItem(str(task[0]) + ' \n ' + str(task[1]))

        self.todo_list.itemDoubleClicked.connect(lambda: self.open_item(self.todo_list.currentItem().text(), self.projectname_combo_box.currentText()))
        self.in_progress_list.itemDoubleClicked.connect(lambda: self.open_item(self.in_progress_list.currentItem().text(), self.projectname_combo_box.currentText()))
        self.done_list.itemDoubleClicked.connect(lambda: self.open_item(self.done_list.currentItem().text(), self.projectname_combo_box.currentText()))


    def open_stats(self):
        self.stats = stats(self.id, self.role, self.id_project)
        self.stats.show()
        self.close()

    def refresh(self):
        self.main_win = main_win(self.role, self.id)
        self.main_win.show()
        self.close()

    def open_reports(self):
        self.mode = 'reports'
        self.reports = reports_backlog(self.mode, self.id_project)
        self.reports.show()

    def open_backlog(self):
        self.mode = 'backlog'
        self.backlog = reports_backlog(self.mode, self.id_project)
        self.backlog.show()

    def open_new_project(self):
        self.new_project = new_project()
        self.new_project.show()

    def open_new_task(self):
        self.new_project = new_task(self.id_project, self.id)
        self.new_project.show()

    def open_item(self, id_of_item, project_name):            
        self.project_name = project_name
        self.id_of_item = id_of_item.split(' ')[0]
        print(self.id_of_item)
        # open task window with id of item
        self.task_window = task(self.id_of_item, self.project_name, self.id_project, self.id)
        self.task_window.show()

    def refresh_lists(self):
        self.todo_list.clear()
        self.in_progress_list.clear()
        self.done_list.clear()
        # query for tasks of project
        self.project_name = self.projectname_combo_box.currentText()
        cur.execute("SELECT projects.id FROM projects left join tasks on projects.id = tasks.project_id WHERE projects.name = %s", (self.project_name,))
        id_projects = cur.fetchall()
        self.id_project = id_projects[0][0]

        cur.execute("SELECT id, name, status FROM tasks WHERE project_id = %s AND status = 'todo' and empl_code = %s", (self.id_project, self.id))
        self.todo_tasks = cur.fetchall()
        for task in self.todo_tasks:
            self.todo_list.addItem(str(task[0]) + ' \n ' + str(task[1]))
        cur.execute("SELECT id, name, status FROM tasks WHERE project_id = %s AND status = 'in progress' and empl_code = %s", (self.id_project, self.id))
        self.in_progress_tasks = cur.fetchall()
        for task in self.in_progress_tasks:
            self.in_progress_list.addItem(str(task[0]) + ' \n ' + str(task[1]))
        cur.execute("SELECT id, name, status FROM tasks WHERE project_id = %s AND status = 'done' and empl_code = %s", (self.id_project, self.id))
        self.done_tasks = cur.fetchall()
        for task in self.done_tasks:
            self.done_list.addItem(str(task[0]) + ' \n ' + str(task[1]))


class reports_backlog(QtWidgets.QDialog, Ui_ReportsWindow):
    def __init__(self, mode, id_project):
        super().__init__()
        self.setupUi(self)
        self.id_project = id_project
        self.mode = mode
        # clear table widget
        self.tableWidget.clear()

        if self.id_project == None:
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setHorizontalHeaderLabels(['No project selected'])
            self.tableWidget.setColumnWidth(0, 800)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('No project selected'))
        elif self.mode == 'reports':
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(['id', 'report', 'date', 'task_id', 'empl_code', 'project_id'])
            self.tableWidget.setColumnWidth(0, 50)
            self.tableWidget.setColumnWidth(1, 550)
            self.tableWidget.setColumnWidth(2, 150)
            self.tableWidget.setColumnWidth(3, 90)
            self.tableWidget.setColumnWidth(4, 90)
            self.tableWidget.setColumnWidth(5, 90)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            cur.execute("SELECT * from reports WHERE project_id = '%s'", (self.id_project,))
            self.reports = cur.fetchall()
            self.tableWidget.setRowCount(len(self.reports))
            for report in self.reports:
                self.report_date = report[2].strftime("%d/%m/%Y")
                self.report_date = self.report_date.split('/')
                self.report_date = self.report_date[2] + '.' + self.report_date[1] + '.' + self.report_date[0]
                self.report_date = self.report_date.replace(' ', '')
            print(self.reports)
            for rows in range(len(self.reports)):
                    for row in range(6):
                        self.tableWidget.setItem(rows, row, QtWidgets.QTableWidgetItem(str(self.reports[rows][row])))
    
        elif self.mode == 'backlog':
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(['id', 'date', 'date_act', 'empl_code'])
            self.tableWidget.setColumnWidth(0, 50)
            self.tableWidget.setColumnWidth(1, 150)
            self.tableWidget.setColumnWidth(2, 150)
            self.tableWidget.setColumnWidth(3, 150)
            self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            cur.execute("SELECT id, date, date_act, empl_code from tasks WHERE status = 'done' and project_id = '%s'", (self.id_project,))
            self.backlog = cur.fetchall()
            print(self.backlog)
            self.tableWidget.setRowCount(len(self.backlog))
            for log in self.backlog:
                self.log_date = log[1].strftime("%d/%m/%Y")
                self.log_date_act = log[2].strftime("%d/%m/%Y")
                self.log_date = self.log_date.split('/')
                self.log_date = self.log_date[2] + '.' + self.log_date[1] + '.' + self.log_date[0]
                self.log_date = self.log_date.replace(' ', '')
                self.log_date_act = self.log_date_act.split('/')
                self.log_date_act = self.log_date_act[2] + '.' + self.log_date_act[1] + '.' + self.log_date_act[0]
                self.log_date_act = self.log_date_act.replace(' ', '')
            for rows in range(len(self.backlog)):
                    for row in range(4):
                        self.tableWidget.setItem(rows, row, QtWidgets.QTableWidgetItem(str(self.backlog[rows][row])))

        

class new_task(QtWidgets.QDialog, Ui_NewTask):
    def __init__(self, id_of_project, code):
        super().__init__()
        self.setupUi(self)
        self.code = code
        self.id_of_project = id_of_project
        print(self.id_of_project)
        self.buttonBox.accepted.connect(self.create_task)
        self.buttonBox.rejected.connect(self.close)
        # get list of users codes from project where user is in project and project is selected
        cur.execute("SELECT codes_users FROM projects WHERE codes_users LIKE %s AND id = %s", ('%' + str(self.code) + '%', self.id_of_project))
        self.codes = cur.fetchall()
        # self.codes to list of integers
        self.codes = self.codes[0][0].split(', ')
        # clear empty
        self.codes = [i for i in self.codes if i]
        # to int
        self.codes = [int(i) for i in self.codes]
        print(self.codes)
        # get all employees names and codes of project
        cur.execute("SELECT name, id FROM users WHERE code = ANY(%s) and role = 'employee'", (self.codes,))
        self.employees = cur.fetchall()
        print(self.employees)
        # employee name to listwidget
        list_of_employee = []
        for employee in self.employees:
            if employee not in list_of_employee:
                list_of_employee.append(employee)
        for employee in list_of_employee:
            self.list_of_employee.addItem(employee[0])

    def create_task(self):
        self.task_status = 'todo'
        self.task_name = self.task_name_input.text()
        self.task_desc = self.task_description_input.text()
        self.task_date = self.dateEdit.text()
        # postgre date format from string
        self.task_date = self.task_date.split('.')
        self.task_date = self.task_date[2] + '-' + self.task_date[1] + '-' + self.task_date[0]
        self.task_date = self.task_date.replace(' ', '')

        self.task_empl_name = self.list_of_employee.currentItem().text()
        for employee in self.employees:
            if employee[0] == self.task_empl_name:
                self.task_empl_code = employee[1]
        
        cur.execute("SELECT max(id) FROM tasks")
        self.max_id = cur.fetchall()
        # self.task_empl_code to int
        self.task_empl_code = int(self.task_empl_code)
        if self.max_id[0][0] == None:
            self.id_of_task = 1
        else:
            self.id_of_task = self.max_id[0][0] + 1
        cur.execute("INSERT INTO tasks (id, name, descr, status, date, empl_code, project_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", (self.id_of_task, self.task_name, self.task_desc, self.task_status, self.task_date, self.task_empl_code, self.id_of_project))
        con.commit()
        self.close()


class task(QtWidgets.QDialog, Ui_TaskWindow):
    def __init__(self, id_of_task, project_name, id_project, code):
        super().__init__()
        self.setupUi(self)
        self.id_of_task = id_of_task
        self.project_name = project_name
        self.id_project = id_project
        self.code = code
        cur.execute("SELECT name, descr, status, date, date_act FROM tasks WHERE id = %s", (self.id_of_task,))
        task_info = cur.fetchall()
        self.task_name = task_info[0][0]
        self.task_desc = task_info[0][1]
        self.task_status = task_info[0][2]
        self.task_date = task_info[0][3]
        self.task_num2.setText(self.id_of_task)
        self.task_name2.setText(self.task_name)
        self.task_desc2.setText(self.task_desc)
        self.task_date = self.task_date.strftime("%d/%m/%Y")
        self.date_to_complete2.setText(self.task_date)
        self.status2.setText(self.task_status)

        if self.task_status == 'todo':
            self.complete_button_2.hide()
            self.complete_button.setText('Take task')
        self.report_button.clicked.connect(self.send_report)
        self.complete_button.clicked.connect(self.complete_task)
        self.ok_button.clicked.connect(self.close)
        self.complete_button_2.clicked.connect(self.decrease_task)

    def send_report(self):
        self.date = datetime.datetime.now()
        # postgre date format from string
        self.date = self.date.strftime("%d/%m/%Y")
        self.date = self.date.split('/')
        self.date = self.date[2] + '-' + self.date[1] + '-' + self.date[0]
        self.date = self.date.replace(' ', '')

        self.report = self.new_report_input.text()
        cur.execute("SELECT max(id) FROM reports")
        self.max_id = cur.fetchall()
        if self.max_id[0][0] == None:
            self.id_of_report = 1
        else:
            self.id_of_report = self.max_id[0][0] + 1
        cur.execute("INSERT INTO reports (id, report, task_id, date, empl_code, project_id) VALUES (%s, %s, %s, %s, %s, %s)", (self.id_of_report, self.report, self.id_of_task, self.date, self.code, self.id_project))
        con.commit()
        self.new_report_input.setText('')

    def complete_task(self):
        if self.task_status == 'todo':
            cur.execute("UPDATE tasks SET status = 'in progress' WHERE id = %s", (self.id_of_task,)) 
            con.commit()
        else:
            date = datetime.datetime.now()
            # postgre date format from string
            date = date.strftime("%d/%m/%Y")
            date = date.split('/')
            date = date[2] + '-' + date[1] + '-' + date[0]
            date = date.replace(' ', '')

            cur.execute("UPDATE tasks SET status = 'done', date_act = %s WHERE id = %s", (date, self.id_of_task))
            con.commit()
        self.close()
    
    def decrease_task(self):
        if self.task_status == 'done':
            cur.execute("UPDATE tasks SET status = 'in progress' WHERE id = %s", (self.id_of_task,))
            con.commit()
        else:
            cur.execute("UPDATE tasks SET status = 'todo' WHERE id = %s", (self.id_of_task,))
            con.commit()
        self.close()

class new_project(QtWidgets.QDialog, Ui_NewProject):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_members.setText('')
        self.codes_selected_members = ''
        self.listWidget.clear()
        # list of all employees and code in listwidget
        cur.execute("SELECT name, code FROM users WHERE role = 'employee'")
        self.employees = cur.fetchall()
        print(self.employees)
        for employee in self.employees:
            self.listWidget.addItem(employee[0])


        self.listWidget.itemDoubleClicked.connect(lambda: self.add_member(self.listWidget.currentItem().text(), self.employees))
        self.buttonBox.accepted.connect(self.create_project)
        self.buttonBox.rejected.connect(self.close)

    def add_member(self, member, employees):
        self.employees = employees
        for employee in self.employees:
            if employee[0] == member:
                self.code = employee[1]
        if member not in self.selected_members.text():
            self.selected_members.setText(self.selected_members.text() + member + '\n')
            self.codes_selected_members = self.codes_selected_members + str(self.code) + ', '
        else:
            self.selected_members.setText(self.selected_members.text().replace(member + '\n', ''))
            self.codes_selected_members = self.codes_selected_members.replace(str(self.code) + ', ', '')

        # print all codes of selected members
        print(self.codes_selected_members)

    def create_project(self):
        cur.execute("SELECT max(id) FROM projects")
        self.max_id = cur.fetchall()
        print(self.max_id[0][0])
        if self.max_id[0][0] is None:
            self.id_of_project = 1
        else:
            self.id_of_project = self.max_id[0][0] + 1
        self.project_name = self.project_name_input.text()
        # add codes of admins to codes of selected members
        cur.execute("SELECT code FROM users WHERE role = 'admin'")
        self.admins = cur.fetchall()
        for admin in self.admins:
            self.codes_selected_members = self.codes_selected_members + str(admin[0]) + ', '
        cur.execute("INSERT INTO projects (id, name, codes_users) VALUES (%s, %s, %s)", (self.id_of_project, self.project_name, self.codes_selected_members))
        con.commit()
        self.close()
        

class sign_in(QtWidgets.QDialog, Ui_SignIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.signin_button.clicked.connect(self.input_checker)


    def input_checker(self):
        if (self.login_input.text() and self.empl_code_input.text()) != '':
            cur.execute("SELECT login FROM users WHERE login = %s or code = %s", (self.login_input.text(), self.empl_code_input.text()))
        else:
            if self.login_input.text() == '':
                self.login_input.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
                self.login_input.setText('')
            elif self.pass_input_2.text() == '':
                self.pass_input_2.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
            elif self.empl_code_input.text() == '':
                self.empl_code_input.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
            elif self.name_input.text() == '':
                self.name_input.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
            elif cur.fetchall() != []:
                self.login_input.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
                self.login_input.setText('')
                self.empl_code_input.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
                self.empl_code_input.setText('')
                self.pass_input_2.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
                self.pass_input.setText('')
                self.name_input.setStyleSheet("border: 1px;\n"
                "border-color: rgb(255, 0, 0);\n"
                "border-style: outset;\n"
                "border-radius: 8px;")
                self.name_input.setText('')
            else:
                self.login = self.login_input.text()
                self.password = self.pass_input_2.text()
                self.empl_code = self.empl_code_input.text()
                self.name = self.name_input.text()
                cur.execute("SELECT max(id) FROM users")
                self.max_id = cur.fetchall()[0][0]
                if self.max_id is None:
                    self.code = 1
                else:
                    self.code = self.max_id + 1
                cur.execute("INSERT INTO users (id, name, login, password, role, code) VALUES (%s, %s, %s, %s, %s, %s)", (self.code, self.name, self.login, self.password, 'employee', self.empl_code))
                con.commit()
                self.login = login()
                self.login.show()
                self.close()


class stats(QtWidgets.QDialog, Ui_Stats):
    def __init__(self, code, role, project_id):
        super().__init__()
        self.setupUi(self)
        self.code = code
        self.role = role
        self.project_id = project_id
        self.active_sprints_button.clicked.connect(self.export)
        self.homepage_button.clicked.connect(self.open_main_win)
        self.refresh_button.clicked.connect(self.refresh)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        # line diagram in widget7 of tasks done by employees in last 7 days if role is admin
        if self.role == 'admin':
            cur.execute("SELECT name, code FROM users")
            self.employees = cur.fetchall()
            self.employees_tasks = []
            for employee in self.employees:
                cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act >= current_date - interval '7 days'", (employee[1],))
                self.employees_tasks.append(cur.fetchall()[0][0])
            self.ax.plot([1, 2, 3, 4, 5, 6, 7], self.employees_tasks)
            self.ax.set_title('Tasks done by employees in last 7 days')
            self.ax.set_xlabel('days')
            self.ax.set_ylabel('tasks done')
            self.figure.set_facecolor('none')
            self.figure.tight_layout()
            self.figure.set_alpha(0)
            # set size of canvas
            self.canvas.resize(750, 340)
            # set margins of canvas to make space for label of x axis
            self.figure.subplots_adjust(bottom=0.15)
            # set x axis to 1-7
            self.ax.set_xlim(1, 7)
            # draw lines of grid
            self.ax.grid(True)
            self.canvas.draw()
            self.layout = QtWidgets.QVBoxLayout(self.widget_7)
            self.layout.addWidget(self.canvas)
        # line diagram in widget7 of tasks done by employee in last 7 days if role is employee
        else:
            # line diagram in widget7 of tasks done by employee in last 7 days
            # list of tasks done by employee in last 7 days day by day with 0 if no tasks done
            self.employees_tasks = []
            cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act = current_date - interval '6 days'", (self.code,))
            self.employees_tasks.append(cur.fetchall()[0][0])
            cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act = current_date - interval '5 days'", (self.code,))
            self.employees_tasks.append(cur.fetchall()[0][0])
            cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act = current_date - interval '4 days'", (self.code,))
            self.employees_tasks.append(cur.fetchall()[0][0])
            cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act = current_date - interval '3 days'", (self.code,))
            self.employees_tasks.append(cur.fetchall()[0][0])
            cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act = current_date - interval '2 days'", (self.code,))
            self.employees_tasks.append(cur.fetchall()[0][0])
            cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act = current_date - interval '1 days'", (self.code,))
            self.employees_tasks.append(cur.fetchall()[0][0])
            cur.execute("SELECT count(id) FROM tasks WHERE empl_code = %s AND status = 'done' AND date_act = current_date", (self.code,))
            self.employees_tasks.append(cur.fetchall()[0][0])
            print(self.employees_tasks)
            self.ax.plot([1, 2, 3, 4, 5, 6, 7], self.employees_tasks)
            self.ax.set_title('Tasks done by you in last 7 days')
            self.ax.set_xlabel('days')
            self.ax.set_ylabel('tasks done')
            self.figure.set_facecolor('none')
            self.figure.tight_layout()
            self.figure.set_alpha(0)
            # set size of canvas
            self.canvas.resize(750, 340)
            # set margins of canvas to make space for label of x axis
            self.figure.subplots_adjust(bottom=0.15)
            # set x axis to 1-7
            self.ax.set_xlim(1, 7)
            # draw lines of grid
            self.ax.grid(True)
            self.canvas.draw()
            self.layout = QtWidgets.QVBoxLayout(self.widget_7)
            self.layout.addWidget(self.canvas)

        # pie diagram in widget8 of tasks status if role is admin on project

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        # set background color of diagram to transparent
        self.figure.set_facecolor('none')
        if self.role == 'admin':
            cur.execute("SELECT count(id) FROM tasks WHERE status = 'todo' AND project_id = %s", (self.project_id))
            self.to_do = cur.fetchall()[0][0]
            cur.execute("SELECT count(id) FROM tasks WHERE status = 'in progress' AND project_id = %s", (self.project_id))
            self.in_progress = cur.fetchall()[0][0]
            cur.execute("SELECT count(id) FROM tasks WHERE status = 'done' AND project_id = %s", (self.project_id))
            self.done_ = cur.fetchall()[0][0]
            self.ax.pie([self.to_do, self.in_progress, self.done_], labels=['todo', 'in progress', 'done'])
            self.ax.set_title('Tasks status')
            self.figure.set_facecolor('none')
            self.figure.set_alpha(0)
            self.canvas.draw()
            self.layout = QtWidgets.QVBoxLayout(self.widget_8)
            self.layout.addWidget(self.canvas)
        # pie diagram in widget8 of tasks status if role is employee on project
        else:
            cur.execute("SELECT count(id) FROM tasks WHERE status = 'todo' AND project_id = %s AND empl_code = %s", (self.project_id, self.code))
            self.to_do = cur.fetchall()[0][0]
            cur.execute("SELECT count(id) FROM tasks WHERE status = 'in progress' AND project_id = %s AND empl_code = %s", (self.project_id, self.code))
            self.in_progress = cur.fetchall()[0][0]
            cur.execute("SELECT count(id) FROM tasks WHERE status = 'done' AND project_id = %s AND empl_code = %s", (self.project_id, self.code))
            self.done_ = cur.fetchall()[0][0]
            print(self.to_do, self.in_progress, self.done_)
            if self.to_do == 0 and self.in_progress == 0 and self.done_ == 0:
                self.ax.pie([1], labels=['no tasks'])
            else:
                self.ax.pie([self.to_do, self.in_progress, self.done_], labels=['todo', 'in progress', 'done'])
                self.ax.set_title('Tasks status')
                self.figure.set_facecolor('none')
                self.figure.set_alpha(0)
            self.canvas.draw()
            self.layout = QtWidgets.QVBoxLayout(self.widget_8)
            self.layout.addWidget(self.canvas)


    def export(self):
        try:
            # export to excel
            print('export')
        except:
            # error message
            print('error')
        # TODO: connect to database

    def open_main_win(self):
        try:
            self.main_win = main_win(role=self.role, id=self.code)
            self.main_win.show()
            self.close()
        except:
            # error message
            print('error')

    def refresh(self):
        self.stats = stats(code=self.code, role=self.role, project_id=self.project_id)
        self.stats.show()
        self.close()
        

# unit tests of qt app
# import unittest
# class TestApp(unittest.TestCase):
#     def test_main_win(self):
#         self.app = QtWidgets.QApplication([])
#         self.assertEqual(main_win(role='admin', id='1').role, 'admin')
#         self.assertEqual(main_win(role='admin', id='1').code, '1')
#         self.assertEqual(main_win(role='admin', id='1').project_id, None)
#         self.assertEqual(main_win(role='employee', id='1').role, 'employee')

#     def test_stats(self):
#         self.app = QtWidgets.QApplication([])
#         self.assertEqual(stats(role='admin', code='1', project_id='1').role, 'admin')
#         self.assertEqual(stats(role='admin', code='1', project_id='1').employees_tasks, [])

# TestApp().test_main_win()
# TestApp().test_stats()

    
app = QtWidgets.QApplication([])

window = login()   

window.show()

sys.exit(app.exec_())