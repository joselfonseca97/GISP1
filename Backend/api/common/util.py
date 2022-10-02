import cloudant.query
from cloudant.document import Document

from api.common.auth import auth


def cloudant_id_validator(db_name, doc_id):
    DB = auth.get_db(db_name)
    return Document(DB, doc_id).exists()


def cloudant_filter(DB, filter, filterType, fields):
        '''
        Make a Cloudant query with filters
        '''
        rows = []
        count = 0
        if filterType == "all":
            query = cloudant.query.Query(DB,
                                         selector={"_id": {"$gt": 0}},
                                         fields=fields)

        elif filterType == 'date':
            dates = filter.split("-")
            start_date = dates[0]
            final_date = dates[1]
            query = cloudant.query.Query(DB,
                                         selector={"$and": [
                                                             {"date": {"$lt": final_date}},
                                                             {"date": {"$gt": start_date}}]},
                                         fields=fields)
        # Emission Factor
        elif filterType == 'year_country':
            filters = filter.split("-")
            year = filters[0]
            country = filters[1]
            query = cloudant.query.Query(DB,
                                         selector={"_id": {"$gt": 0}},
                                         fields=fields)

            for factor in query.result:
                for c in factor['countries']:
                    if c == country:
                        for y in factor['years']:
                            if y == year:
                                rows.append(factor)
                                count += 1

            return {
                "data": rows,
                "total": count
            }
        else:
            query = cloudant.query.Query(DB,
                                         selector={filterType: {"$regex": filter}},
                                         fields=fields)
        print(query)
        for doc in query.result:
                print(doc)
                rows.append(doc)
                count += 1
        res = {
                "data": rows,
                "total": count
        }

        return res

