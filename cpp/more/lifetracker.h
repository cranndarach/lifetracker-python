#pragma once
#include <QObject>
#include <QMainWindow>
#include <QWidget>
#include <QString>
#include <iostream>

class Lifetracker: public QMainWindow
{
Q_OBJECT

public:
    Lifetracker(QMainWindow *parent = 0);
    ~Lifetracker();

public slots:
    void on_bEvent_clicked();
    void on_bTask_clicked();
    void on_bExp_clicked();
    //void on_bSimple_clicked();
    void on_bSleep_clicked();

protected:
    // int mainPosn, inflPosn, statusPosn = 0;
};
