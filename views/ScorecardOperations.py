from scorecard_backend.database.DBConnection import databaseOperation, databaseOperationSave
from scorecard_backend.models.Configuration import Configuration
import json





def getByAge(age):
    sql = "SELECT cs.criteria, (CONVERT(cs.score, DECIMAL(10,2)) * CONVERT(a.weightage , DECIMAL(10,2))) as mul " \
          "FROM mifostenant.m_criteriascore as cs, mifostenant.m_configuration a " \
          "where cs.cscriteriatableid = a.id and  a.feature = 'Age' and cs.cscriteriatableid=1"
    result = databaseOperation(sql)
    score = 0
    if(result):
        for row in result:
            criteria = row[0]
            minage, maxage = criteria.split('-')
            if(age >= int(minage) and age <= int(maxage)):
                score = float(row[1])
                break
    return score

def getByGender(gender):
    sql = "SELECT cs.criteria, (CONVERT(cs.score, DECIMAL(10,2)) * CONVERT(a.weightage , DECIMAL(10,2))) as mul " \
          "FROM mifostenant.m_criteriascore as cs, mifostenant.m_configuration a " \
          "where cs.cscriteriatableid = a.id and  Upper(a.feature)= 'GENDER' and cs.cscriteriatableid=2"
    result = databaseOperation(sql)
    score = 0
    if(result):
        for row in result:
            criteria = row[0]
            if(criteria.upper() == gender):
                score = float(row[1])
                break
    return score


