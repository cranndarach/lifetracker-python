#ifndef ENTRY_H
#define ENTRY_H

#include <QDialog>
#include <QFormLayout>
#include <fstream>
#include <iostream>

class Entry: public QDialog
{
public:
    // explicit
    Entry(QDialog *parent = 0);
    // ~Entry(); // destructor
    // template <class T>
    // void addLine(std::string label, T *ent);
    void populate();
    // void processData();
    // void saveData();
    // void count();
    QFormLayout *frm = new QFormLayout(this);

private:

};

#endif // ENTRY_H
