import datetime, uuid
from pydantic import BaseModel
from .enumerators import StatesBrEnum as StatesEnum


class UserBase(BaseModel):
    name: str
    email: str


class User(UserBase):
    user_id: (uuid.uuid1(str))
    phone: str
    document_number: str
    doc_type: str
    balance: float


class register_user(UserBase):
    passord: str


class Vehicle(BaseModel):
    vehicle_id: (uuid.uuid1(str))
    board: str
    model: str
    like_vehicle: str


class register_vehicle(Vehicle):
    passar


class Reservation(BaseModel):
    reservation_id: (uuid.uuid1(str))
    start_time: datetime
    hour_find: datetime


class booking_vacancies(Reservation):
    passar


class Recharge(BaseModel):
    load_id: (uuid.uuid1(str))
    data: datetime
    value: float
    quantity_time: int
    payment_status: bool
    vehicle_type: str
    payment_type: str


class recharger_do(Recharge):
    passar


class Biullet(BaseModel):
    id_boleto: (uuid.uuid1(str))
    barcode: str
    expiration_date: datetime.data


class creat_ticket(Boleto):
    passar


class Card(BaseModel):
    id_cartao: (uuid.uuid1(str))
    hash_cartao: str
    flag: str
    last_digits: int


class register_card(Card):
    passar


class employee(UserBase):
    employee_id: (uuid.uuid1(str))


class register_employees(employee):
    password: str


class new_veicle(Vehicle):
    state: StatesEnum


class uodate_user(User):
    state: StatesEnum

class update_vehicle():
        veicle_id: str = ''
        board: str = ''
        model: str = ''
        like_vehicle: str = ''
