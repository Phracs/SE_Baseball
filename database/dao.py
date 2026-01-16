from database.DB_connect import DBConnect

class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT(year) FROM team where year >=1980"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_squadre_per_anno(anno:int):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT(team_code) FROM team where year = %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row["team_code"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_salario_squadre(anno:int):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT DISTINCT(t.team_code), SUM(s.salary) as salario_tot
                    FROM team t, salary s 
                    where t.team_code = s.team_code
                    and t.year = %s
                    group by t.team_code
                 """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append((row["team_code"], row["salario_tot"]))

        cursor.close()
        conn.close()
        return result