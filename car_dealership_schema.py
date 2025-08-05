from sqlalchemy import create_engine, String, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import date

engine = create_engine('sqlite:///car_dealership.db')

class Base(DeclarativeBase):
    pass

class Salesperson(Base):
    __tablename__ = "salespeople"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    cars = relationship("Car", back_populates="salesperson")
    invoices = relationship("Invoice", back_populates="salesperson")

class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String, nullable=False)
    cars = relationship("Car", back_populates="customer")
    invoices = relationship("Invoice", back_populates="customer")
    service_tickets = relationship("ServiceTicket", back_populates="customer")

class Car(Base):
    __tablename__ = "cars"
    id: Mapped[int] = mapped_column(primary_key=True)
    vin: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    make: Mapped[str] = mapped_column(String)
    model: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    salesperson_id: Mapped[int] = mapped_column(ForeignKey("salespeople.id"))
    customer = relationship("Customer", back_populates="cars")
    salesperson = relationship("Salesperson", back_populates="cars")
    service_tickets = relationship("ServiceTicket", back_populates="car")
    mechanic_links = relationship("MechanicCarLink", back_populates="car")

class Invoice(Base):
    __tablename__ = "invoices"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[date] = mapped_column(Date)
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id"))
    salesperson_id: Mapped[int] = mapped_column(ForeignKey("salespeople.id"))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    salesperson = relationship("Salesperson", back_populates="invoices")
    customer = relationship("Customer", back_populates="invoices")

class Mechanic(Base):
    __tablename__ = "mechanics"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    specialty: Mapped[str] = mapped_column(String, nullable=True)
    car_links = relationship("MechanicCarLink", back_populates="mechanic")

class MechanicCarLink(Base):
    __tablename__ = "mechanic_car_link"
    id: Mapped[int] = mapped_column(primary_key=True)
    mechanic_id: Mapped[int] = mapped_column(ForeignKey("mechanics.id"))
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id"))
    mechanic = relationship("Mechanic", back_populates="car_links")
    car = relationship("Car", back_populates="mechanic_links")

class ServiceTicket(Base):
    __tablename__ = "service_tickets"
    id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey("cars.id"))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    description: Mapped[str] = mapped_column(String)
    date: Mapped[date] = mapped_column(Date)
    car = relationship("Car", back_populates="service_tickets")
    customer = relationship("Customer", back_populates="service_tickets")

Base.metadata.create_all(engine)
