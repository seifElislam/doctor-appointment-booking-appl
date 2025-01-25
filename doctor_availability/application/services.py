"""
Module use cases
"""
from doctor_availability.application.dto import Doctor, Slot
from doctor_availability.infrastructure import models


def list_doctors():
    """

    :return:
    """
    return models.Doctor.objects.all()


def add_doctor(doctor: Doctor):
    """

    :param doctor:
    :return:
    """
    models.Doctor.objects.create(name=doctor.name, specialization=doctor.specialization)


def get_doctor_by_id(id):
    """

    :return:
    """
    return models.Doctor.objects.get(id=id)


def list_doctor_avail_slots(doctor_id):
    """

    :param doctor_id:
    :return:
    """
    doctor_db_obj = get_doctor_by_id(doctor_id)
    return models.Slot.objects.filter(doctor=doctor_db_obj, is_reserved=False)


def add_slot(slot: Slot, doctor: Doctor):
    """

    :param slot:
    :param doctor:
    :return:
    """
    doctor_db_obj = get_doctor_by_id(doctor.id)
    models.Slot.objects.create(doctor=doctor_db_obj, cost=slot.cost, is_reserved=slot.is_reserved)


def update_slot(slot: Slot):
    slot_db_obj = models.Slot.objects.get(id=slot.id)
    slot_db_obj.cost = slot.cost
    slot_db_obj.is_reserved = slot.is_reserved
    slot_db_obj.save()
    return slot_db_obj
