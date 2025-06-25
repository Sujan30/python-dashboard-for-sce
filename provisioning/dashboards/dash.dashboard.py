from grafanalib.core import RowPanel, TimeSeries, Target, Dashboard, Stat, GridPos,Threshold
from dataclasses import dataclass
from grafanalib.formatunits import (
    SECONDS,
    NUMBER_FORMAT,
    BYTES,
    BITS_SEC,
)


class CharacterLiteral:
    def __init__(self):
        self.index = 0
    
    def Next(self):
        val  = chr(65+self.index)
        self.index = (self.index+1)%26
        return val



@dataclass
class pair():
    query: str
    label: str





class Dash:
    
    
    def __init__(self):
        self.rows = []
        self.lastest_row = None
        self.panels = []
        self.Dashboard = None

    def DefineRow(self, title: str):
        row = RowPanel(title= title, panels=[])
        self.rows.append(row)
        self.lastest_row = row
    

    def AddPanelToRow(self, title: str, array: list[pair] ):
        if self.lastest_row is None:
            raise ValueError('No rows, call define row first')
        
        char_iter = CharacterLiteral()
        
        targets = []
        for pair in array:
            targets.append(Target(
                expr=pair.query, 
                legendFormat= pair.label, 
                refId=char_iter.Next()
            ))
        panel = [
            Stat(
                title=title,
                reduceCalc='lastNotNull', 
                format=SECONDS,
                gridPos=GridPos(h=8, w=12, x=0, y=0),
                thresholds=[
                    Threshold('green', 0, 0.0),
                ],
                targets=targets
                    
            )
        ]
        self.lastest_row.panels.extend(panel)
        self.panels.extend(panel)
    
    def AddPanel(self, title: str, array: list[pair]):
        char_iter = CharacterLiteral()
        
        targets = []
        for pair in array:
            targets.append(Target(
                expr=pair.query, 
                legendFormat= pair.label, 
                refId=char_iter.Next()
            ))
        panel = [
            Stat(
                title=title,
                reduceCalc='lastNotNull', 
                format=SECONDS,
                gridPos=GridPos(h=8, w=12, x=0, y=0),
                thresholds=[
                    Threshold('green', 0, 0.0),
                ],
                targets=targets
                    
            )
        ]
        
        self.panels.append(panel)
        
    def Render(self, title):
        self.DashBoard = Dashboard(
            title=title, 
            uid="dashboard", 
            timezone='browser',
            panels=self.panels + [panel for row in self.rows for panel in row.panels]
        ).auto_panel_ids()



dash = Dash()
dash.DefineRow('my new row')
dash.AddPanelToRow("My first panel", [pair("query", "label")])
dash.Render("My New Dashboard")
dashboard = dash.DashBoard







            

            


        



        





