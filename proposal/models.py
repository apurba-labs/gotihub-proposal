from pydantic import BaseModel


class Company(BaseModel):
    name: str
    tagline: str
    website: str
    email: str
    phone: str
    address: str


class Client(BaseModel):
    name: str
    contact: str


class Proposal(BaseModel):
    title: str
    subtitle: str
    prepared_date: str
    timeline: str
    price: str


class ProposalData(BaseModel):
    company: Company
    client: Client
    proposal: Proposal