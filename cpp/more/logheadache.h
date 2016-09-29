#ifndef LOGHEADACHE_H
#define LOGHEADACHE_H

#include "entry.h"

class LogHeadache: public Entry {
public:
    // explicit
    LogHeadache(Entry *parent = 0);
    ~LogHeadache(); // destructor
};


#endif // LOGHEADACHE_H
