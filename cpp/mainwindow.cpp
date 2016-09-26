#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "logevent.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent)
{
    setupUi(this);
}

void MainWindow::on_log_event_clicked()
{
    LogEvent e;
    e.exec();
}

MainWindow::~MainWindow() {}
