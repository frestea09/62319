from __future__ import print_function
from abc import ABCMeta,abstractmethod
import psycopg2
class KerangkaMahasiswa(metaclass=ABCMeta):
    @abstractmethod
    def tambahMahasiswa(self):
        pass
    @abstractmethod
    def updateMahasiswa(self):
        pass
    @abstractmethod
    def deleteMahasiswa(self):
        pass
class Mahasiswa(KerangkaMahasiswa):
    def __init__(self,insertDBName=None,insertUser=None,insertPassword=None,insertNim=None,insertName=None,insertAddress=None,insertGender=None,insertStatus=None):
        self.__nim = insertNim
        self.__name = insertName
        self.__address = insertAddress
        self.__gender = insertGender
        self.__status = insertStatus
        self.__dbname = insertDBName
        self.__user = insertUser
        self.__password = insertPassword
    def setNim(self,insertNim):
        self.__nim = insertNim
    def getNim(self):
        return self.__nim
    def setName(self,insertName):
        self.__name  = insertName
    def getName(self):
        return self.__name
    def setAddress(self,insertAddress):
        self.__address = insertAddress
    def getAddress(self):
        return self.__address
    def setGender(self,insertGender):
        self.__gender = insertGender
    def getGender(self):
        return self.__gender
    def setStatus(self,insertStatus):
        self.__status = insertStatus
    def getStatus(self):
        return self.__status
    def setDbName(self,insertDbName):
        self.__dbname = insertDbName
    def getDbName(self):
        return self.__dbname
    def setUser(self,insertUser):
        self.__user = insertUser
    def getUser(self):
        return self.__user
    def setPassword(self,insertPassword):
        self.__password = insertPassword
    def getPassword(self):
        return self.__password
    def tambahMahasiswa(self):
        dbName = self.__dbname
        user = self.__user
        password = self.__password
        try:
            conn = psycopg2.connect(
                dbName=dbName,
                user=user,
                password=password
            )
            cur = conn.cursor()
            sql = '''
                SELECT * FROM table_mahasiswa
            '''
            cur.execute(sql)
            result = cur.fetchall()
            for element in result:
                mahasiswaId = element[0]
                mahasiswaNama = element[1]
                mahasiswaGender = element[2]
                mahasiswaStatus = element[3]
                mahasiswaAddress = element[4]
                print('%s %s %s %s %s'%(mahasiswaId,mahasiswaNama,mahasiswaGender,mahasiswaStatus,mahasiswaAddress))
                cur.close()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed')
    def updateMahasiswa(self):
        pass
    def deleteMahasiswa(self):
        pass
def main():
    myMahasiswa = Mahasiswa()

if __name__ == "__main__":
    main()
