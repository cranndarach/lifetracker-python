#pragma once
#include <QMainWindow>
#include <QWidget>
#include <QGridLayout>
#include <QString>
#include <QPushButton>
#include <iostream>

class Lifetracker: public QMainWindow {
public:
    Lifetracker(QMainWindow *parent = 0);
    // QPushButton* addButton(QString label, QWidget *tab, QGridLayout *grid, int posn);

private slots:
    void on_bEvent_clicked();

private:
    // int mainPosn, inflPosn, statusPosn = 0;
};
