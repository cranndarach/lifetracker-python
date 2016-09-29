#ifndef LOGHUNGER_H
#define LOGHUNGER_H

#include "entry.h"

class LogHunger: public Entry {
public:
    // explicit
    LogHunger(Entry *parent = 0);
    ~LogHunger(); // destructor
};


#endif // LOGHUNGER_H
