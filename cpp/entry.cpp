#include "entry.h"

Entry::Entry(QWidget *parent):
    QDialog(parent)
{
    setupUi(this);
}

template <class T>
void Entry::add_line(string label, T) {
    QLabel *lbl = new QLabel(this);
    lbl->setText(label);
    T ent = new T(this);
    // set placement in grid

}
