#ifndef LOGTASK_H
#define LOGTASK_H

#include "entry.h"

class LogTask: public Entry {
public:
    // explicit
    LogTask(Entry *parent = 0);
    ~LogTask(); // destructor
};
#endif // LOGTASK_H
