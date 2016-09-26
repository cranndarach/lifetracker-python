#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "ui_mainwindow.h"
#include <QMainWindow>

//namespace Ui {
//class MainWindow;
//}


class MainWindow : public QMainWindow, private Ui::MainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_log_event_clicked();

//private:
//    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
