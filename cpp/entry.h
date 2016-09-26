#ifndef ENTRY_H
#define ENTRY_H

#include <QObject>
#include <QWidget>
#include <QLabel>
#include <fstream>
#include <string>

class Entry: public QDialog
{
public:
    explicit Entry(QWidget *parent = 0);
    ~Entry();
//    void add_line(string label, T){
//        QLabel *lbl = new QLabel(this);
//        lbl->setText(label);
//        T ent = new T(this);

//    }
//    void add_datetime(){}
    void add_line() {}
    void process_data() {}
    void save_data() {}
    void count() {}

private:
    int row = 0, col = 0, rowmaster = 0, colmaster = 0;
};

#endif // ENTRY_H
