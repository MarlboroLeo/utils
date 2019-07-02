# coding=utf-8
# @Time    : 2019/5/16 16:08
# @Author  : Leau
# @File    : models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, MetaData, ForeignKey, Boolean, LargeBinary

Base = declarative_base()


# 主机模型
class DuBang(Base):
    __tablename__ = 'dbic_copy'

    id = Column(Integer, primary_key=True)
    insur_id = Column(String(50))  # 保单号
    insur_starttime = Column(String(50))  # 商业险起始日期
    insur_endtime = Column(String(50))  # 商业险截止日期
    insured_name = Column(String(100))  # 投保人名称
    assured = Column(String(100))  # 被保人名称
    assure_cer = Column(String(100))  # 被保人证件号
    car_num = Column(String(100))  # 车牌号
    frame_num = Column(String(100))  # 车架号
    engine_num = Column(String(100))  # 发动机号
    paid_premium = Column(String(255))  # 已缴纳合计
    special_promise = Column(String(1024))  # 特别约定 (受益人)
    compulsory = Column(String(100))  # 交强险金额
    tax = Column(String(100))  # 车船税
    epolicy_bit = Column(LargeBinary(length=16777216))  # 保单


class SunShine(Base):
    __tablename__ = 'sunshine_copy'

    id = Column(Integer, primary_key=True)
    insur_id = Column(String(50), primary_key=True)  # 保单号
    insur_starttime = Column(String(200))  # 商业险起始日期
    insur_endtime = Column(String(252))  # 商业险截止日期
    insured_name = Column(String(100))  # 投保人名称
    assured = Column(String(100))  # 被保人名称
    assured_cer = Column(String(255))  # 被保人证件号
    car_num = Column(String(100))  # 车牌号
    frame_num = Column(String(100))  # 车架号
    engine_num = Column(String(100))  # 发动机号
    paid_premium = Column(String(255))  # 已缴纳合计
    special_promise = Column(String(500))  # 特别约定 (受益人)
    compulsory = Column(String(100))  # 交强险金额
    tax = Column(String(100))  # 车船税
    epolicy_bit = Column(LargeBinary(length=16777216))  # 保单


class TianPing(Base):
    __tablename__ = 'tianping_copy'

    id = Column(Integer, primary_key=True)
    insur_id = Column(String(50))  # 保单号
    insur_starttime = Column(String(50))  # 商业险起始日期
    insur_endtime = Column(String(50))  # 商业险截止日期
    insured_name = Column(String(100))  # 投保人名称
    assured = Column(String(100))  # 被保人名称
    assure_cer = Column(String(100))  # 被保人证件号
    car_num = Column(String(100))  # 车牌号
    frame_num = Column(String(100))  # 车架号
    engine_num = Column(String(100))  # 发动机号
    paid_premium = Column(String(255))  # 已缴纳合计
    special_promise = Column(String(255))  # 特别约定 (受益人)
    compulsory = Column(String(100))  # 交强险金额
    tax = Column(String(100))  # 车船税
    epolicy_bit = Column(LargeBinary(length=16777216))  # 保单


class TaiPingyang(Base):
    __tablename__ = 'tpy_copy'

    id = Column(Integer, primary_key=True)
    insur_id = Column(String(50))  # 保单号
    insur_starttime = Column(String(50))  # 商业险起始日期
    insur_endtime = Column(String(200))  # 商业险截止日期
    insured_name = Column(String(100))  # 投保人名称
    assured = Column(String(100))  # 被保人名称
    assured_cer = Column(String(100))  # 被保人证件号
    car_num = Column(String(100))  # 车牌号
    frame_num = Column(String(100))  # 车架号
    engine_num = Column(String(100))  # 发动机号
    paid_premium = Column(String(255))  # 已缴纳合计
    special_promise = Column(String(255))  # 特别约定 (受益人)
    compulsory = Column(String(50))  # 交强险
    tax = Column(String(50))  # 车船税
    epolicy_bit = Column(LargeBinary(length=16777216))  # 保单


class Picc(Base):
    __tablename__ = 'picc_copy'

    id = Column(Integer, primary_key=True)
    insur_id = Column(String(50))  # 保单号
    insur_starttime = Column(String(50))  # 商业险起始日期
    insur_endtime = Column(String(200))  # 商业险截止日期
    insured_name = Column(String(100))  # 投保人名称
    assured = Column(String(100))  # 被保人名称
    assured_cer = Column(String(100))  # 被保人证件号
    car_num = Column(String(100))  # 车牌号
    frame_num = Column(String(100))  # 车架号
    engine_num = Column(String(100))  # 发动机号
    paid_premium = Column(String(255))  # 已缴纳合计
    special_promise = Column(String(255))  # 特别约定 (受益人)
    compulsory = Column(String(50))  # 交强险
    tax = Column(String(50))  # 车船税
    epolicy_bit = Column(LargeBinary(length=16777216))  # 保单


class DaDi(Base):
    __tablename__ = 'dadi_copy'

    id = Column(Integer, primary_key=True)
    insur_id = Column(String(50))  # 保单号
    insur_starttime = Column(String(50))  # 商业险起始日期
    insur_endtime = Column(String(200))  # 商业险截止日期
    insured_name = Column(String(100))  # 投保人名称
    assured = Column(String(100))  # 被保人名称
    assured_cer = Column(String(100))  # 被保人证件号
    car_num = Column(String(100))  # 车牌号
    frame_num = Column(String(100))  # 车架号
    engine_num = Column(String(100))  # 发动机号
    paid_premium = Column(String(255))  # 已缴纳合计
    special_promise = Column(String(255))  # 特别约定 (受益人)
    compulsory = Column(String(50))  # 交强险
    tax = Column(String(50))  # 车船税
    epolicy_bit = Column(LargeBinary(length=16777216))  # 保单

