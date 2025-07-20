import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.api import app

def test_reserva_exitosa():
    cliente = app.test_client()
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 201

def test_reserva_duplicada():
    cliente = app.test_client()
    cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    resp = cliente.post('/reservar', json={"sala": "B", "hora": "14:00"})
    assert resp.status_code == 409