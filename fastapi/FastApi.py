from typing import Optional
from dhcp_lease import lease
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
dhcp='dhcpd.leases'
@app.get("/api")
async def parse_ip():
    dict_ip=lease(dhcp)

    return dict_ip


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})


@app.get("/ip", response_class=HTMLResponse)
async def sort_ip(request: Request):
    list_ip = lease(dhcp)
    sort_list_by_ip = sorted(list_ip, key=lambda k: k['ip'])
    return templates.TemplateResponse("dhcp.html", {"request": request, "list_ip": sort_list_by_ip})


@app.get("/hostname", response_class=HTMLResponse)
async def sort_hostname(request: Request):
    list_ip = lease(dhcp)
    sort_list_by_hostname = sorted(list_ip, key=lambda k: k['hostname'], reverse=True)
    return templates.TemplateResponse("dhcp.html", {"request": request, "list_ip": sort_list_by_hostname})

@app.get("/hw", response_class=HTMLResponse)
async def sort_hw(request: Request):
    list_ip = lease(dhcp)
    sort_list_by_hw = sorted(list_ip, key=lambda k: k['hw'])
    return templates.TemplateResponse("dhcp.html", {"request": request, "list_ip": sort_list_by_hw})


""" 
#вывод по id
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
"""

