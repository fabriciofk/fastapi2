"""/ cadastrarVeículo -> receber informações do veículo e cadastrar o veículo no banco.
Receber: placa - string - body
	 modelo - string - corpo
 	 tipo_veiculo - string / enum - corpo
	 id_usuario - int - corpo
Devolver: código de status (200/300/400)
###################################################################
/ editarVeiculo -> Receber as novas informações do veículo e fazer mudanças no banco.
Receber: placa - string - parâmetros de consulta
	 modelo - string - corpo
	 tipo_veiculo - string / enum - corpo
	 id_usuario - int - corpo
Devolver: código de status (200/300/400)
#############################################################
/ excluirVeiculo -> Receber a placa do veículo e excluí-lo
Receber: placa_carro - string - parâmetros de consulta
Devolver: código de status (200/300/400)
"""

from typing import Generator

from sqlalchemy import Session
from .base_schemas import Vehicle
from .base_schemas import register_vehicle

def retrieve_vehicle(db: Session, vehicle_id: str):
return db.query(vehicle).filter(vehicle.id == vehicle_id).first()


def vehicle_register(db: Session, vehicle: update_vehicle):
    """Creates a new vehicle registration from data sent via API"""
    new_vehicle = vehicle(**vehicle.dict())
    db.add(new_vehicle)
    db.commit()

    db.reflesh(new_vehicle)
    return new_vehicle

def update_vehicle(
        db:Session, board: str, values: UpdatevahicleValuesType
):
    if student := vehicle_register(db, vehicle_id):
        db.query(retrieve_vehicle()).filter(update_vehicle==update_vehicle).update(values)
        db.commit()
        db.reflesh(update_vehicle)


def remove_vehicle(db: Session, vehicle_id: str) -> bool:
    if vehicle := retrieve_vehicle(db, vehicle_id):
    db.delete(vehicle)
    db.commit()

    return True

    return Falseclass Veicle(BaseModel):
    veicle_id: (uuid.uuid1(str))
    board: str
    model: str
    like_vehicle: str