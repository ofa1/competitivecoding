/**
 * @param {string} time
 * @return {string}
 */
var nextClosestTime = function(time) {
    var arrT = time.split(':');
    var hours = Number(arrT[0]);
    var minutes = Number(arrT[1]);

    var abcd = getABCD(hours, minutes);
    arrT = [abcd.A, abcd.B, abcd.C, abcd.D];
    var minTime = {hours: hours, minutes: minutes};
    var minTimeDiff = 24 * 60;
    var currTimeDiff = 0;
    var newTime;
    console.log("array is: ", arrT)
    for(var i=0; i<4 ; i++) {
        for(var j=0; j<4; j++) {
            for(var k=0; k<4; k++) {
                for(var l=0; l<4; l++) {
                    newTime = toTimeABCD(arrT[i], arrT[j], arrT[k], arrT[l])
                    if(isNaN(newTime.hours) || isNaN(newTime.minutes) 
                        || 
                        !isValidTime(newTime.hours, newTime.minutes)) {
                        continue;
                    }
                    currTimeDiff = timeDiff(hours, minutes, newTime.hours, newTime.minutes)
                    if(currTimeDiff <= 0) {
                        currTimeDiff += 24 * 60
                    }
                    console.log(newTime, currTimeDiff);
                    if( !isNaN(currTimeDiff) && currTimeDiff != 0 && currTimeDiff < minTimeDiff  ) {
                        minTimeDiff = currTimeDiff;
                        minTime = newTime;
                        // console.log("Min time found: ", newTime, currTimeDiff);                              
                    }
                }
            }
        }
    }
    hours = minTime.hours < 10 ? "0" + minTime.hours : minTime.hours;
    minutes = minTime.minutes < 10 ? "0" + minTime.minutes : minTime.minutes;
    return hours + ":" + minutes
};

function timeDiff(h1, m1, h2, m2) {
    return (new Date(0,0,0,h2, m2, 0,0) - new Date(0,0,0,h1,m1,0,0)) / 60 /1000
}

function toTimeABCD(A,B,C,D) {
    return {
        hours : (A*10) + B,
        minutes : (C*10) + D
    }
}

function getABCD(hours, minutes) {
    return {
        A : ~~(hours / 10),
        B: hours % 10, 
        C: ~~(minutes / 10),
        D: minutes % 10
    }
}

function isValidTime(hours, minutes) {
    if (hours < 24  && hours >= 0 && minutes < 60 && minutes >= 0) {
        return true;
    }
    return false;
}


console.log(nextClosestTime("11:11"))