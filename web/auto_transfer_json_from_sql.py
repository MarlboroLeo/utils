# coding=utf-8
# @Time    : 2019/5/17 17:44
# @Author  : Leau
# @File    : transfer.py
import base64
import json



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine, MetaData, Column, Integer, String, LargeBinary, Binary)
from datetime import datetime


Base = declarative_base()

def get_Session():
    # engine = create_engine('mysql://root:root@172.30.36.7/ivcs_portal?charset=utf8')
    engine = create_engine('mysql+pymysql://root:123456@192.168.1.20/BaoXian?charset=utf8')
    Base.metadata.create_all(engine)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return Session


from sqlalchemy.ext.declarative import DeclarativeMeta


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        elif isinstance(data, bytes):
                            # data = base64.b64encode(data).decode("utf-8")
                            data = None
                        # json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder


def to_json(model_name, insur_id):
    session = get_Session()()
    # vmcs = session.query(VirtualMachineContainer).all()
    # vmcs = session.query(model_name).all()
    vmcs = session.query(model_name).filter_by(insur_id=insur_id)
    # print(vmcs)
    try:

        Hosts = []
        for vmc in vmcs:
            # print json.dumps(vmc, cls=AlchemyEncoder)
            Hosts.append(vmc)
        # print(Hosts)
        # print(json.dumps(Hosts, cls=new_alchemy_encoder(), check_circular=False, ensure_ascii=False))
        return json.dumps(Hosts, cls=new_alchemy_encoder(), check_circular=False, ensure_ascii=False)
        # print(json.dumps(j, ensure_ascii=False))
    except Exception as e:
        print(e)



# if __name__ == '__main__':
#     data = to_json(VirtualMachineContainer)
#     data = json.loads(data)
#     data2 = base64.b64decode(data[0].get("epolicy_bit").encode("utf-8"))
#     with open("tst.pdf", 'wb')as f:
#         f.write(data2)