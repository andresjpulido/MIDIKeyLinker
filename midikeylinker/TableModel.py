from PyQt6.QtCore import Qt, QAbstractTableModel ,QSize
from PyQt6.QtGui import QColor, QFont 

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        value = self._data.iloc[index.row(), index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return str(value)
        
        if role == Qt.ItemDataRole.TextAlignmentRole:

            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str): 
                return Qt.AlignmentFlag.AlignVCenter + Qt.AlignmentFlag.AlignLeft
            
        if role == Qt.ItemDataRole.ForegroundRole:
            return QColor('#DDD')
         
          
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal : 
                return  self._data.columns[section]
        if role == Qt.ItemDataRole.ForegroundRole:
            return QColor('#000') 
        if role == Qt.ItemDataRole.BackgroundRole:
            return QColor('#DDD')

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]