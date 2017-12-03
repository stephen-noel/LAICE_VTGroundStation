# Hello World program in Python

import sys
import binascii
import struct
import codecs
import binascii
import io
import pymysql
import datetime

resp = bytearray.fromhex("43020100800601788000800c80068005c072c08fc0d18056800480128005800685ab00fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffa88a0001a09006e5e3dd12a20d1bb00277a3002b0ba41eb")

cmd = arr = bytearray.fromhex("43020100800601788000800c")

conn = pymysql.connect(host="128.173.144.54",
                       user="root",
                       passwd="wE8piWXGJk*",
                       db="moc_vt_clone")
time = '20171101185455'

def insert_one_record(cmd, resp, time, conn):
    f = io.BytesIO(resp)
    temp = io.BytesIO(resp)
    instrumentLIIB = struct.unpack('>35B', temp.read(35))[0]
    instrumentRPA = struct.unpack('>279B', temp.read(279))[0]
    instrumentSNeuPI = struct.unpack('>35B', temp.read(35))[0]
    instrumentLINAS = struct.unpack('>24B', temp.read(24))[0]
    id = 10
    orbitElapsedTime= 12.5
    orbitNumber=1
    packetID = 1
    createdAt = datetime.datetime.now()
    updatedAt = createdAt
    satelliteUTCTime = datetime.datetime.strptime(time, '%Y%m%d%H%M%S')
    cur = conn.cursor()

    '''
    Level 0 - upload data file
    '''
    # Byte Count
    byte_fmt = '>B'  # for unsigned one byte
    short_fmt = '>H'  # for unsigned two bytes
    byte_fmts = '>b'  # for signed one byte
    short_fmts = '>h'  # for signed two bytes
    '''
    Level 1 - LIIB

    '''
    LIIB_startWordLIIB_L1_Dec = struct.unpack(byte_fmts, f.read(1))[0]
    LIIB_startWordLIIB_L1 = hex(LIIB_startWordLIIB_L1_Dec)  # OUTPUT AS HEX DATA
    LIIB_LIIBModeOpMode = struct.unpack(byte_fmts, f.read(1))[0]  # 1 byte to split
    LIIB_LIIBMode_L1 = (LIIB_LIIBModeOpMode >> 3) & 0b11111  # 0x1f # int("1f", 16.0), rs 3 mask 5
    LIIB_opMode_L1 = (LIIB_LIIBModeOpMode) & 0b111  # 0x07, rs 0 mask 3
    LIIB_pos_5VD_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_3_3V_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_12V_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_5VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_5VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_15VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_15VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_temperatureMonitor3LB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_temperatureMonitor2LB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_temperatureMonitor1LB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_5VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_15VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_5VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_15VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_thermalKnife1VoltageMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_thermalKnife2VoltageMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_Knife1234Status_ToggleStatus = struct.unpack(byte_fmts, f.read(1))[0]  # 1 byte to split, last 3 bits are unused
    LIIB_thermalKnife1Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 7) & 0b1  # rs 7 mask 1
    # print(LIIB_thermalKnife1Status_L1)
    LIIB_thermalKnife2Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 6) & 0b1  # rs 6 mask 1
    LIIB_thermalKnife3Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 5) & 0b1  # rs 5 mask 1
    LIIB_thermalKnife4Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 4) & 0b1  # rs 4 mask 1
    LIIB_tkOverrideToggleStatus_L1 = (LIIB_Knife1234Status_ToggleStatus >> 3) & 0b1  # rs 3 mask 1
    unused_L1 =  (LIIB_Knife1234Status_ToggleStatus) & 0b111
    '''
    Level 2 - LIIB, convert to ASCII
    '''
    LIIB_startWordLIIB_L2 = str(chr(LIIB_startWordLIIB_L1_Dec))  # varchar
    LIIB_LIIBMode_L2 = str(chr(LIIB_LIIBMode_L1))  # varchar
    LIIB_opMode_L2 = str(chr(LIIB_opMode_L1))  # varchar
    LIIB_pos_5VD_MonitorLB_L2 = ((LIIB_pos_5VD_MonitorLB_L1 * 5.0 / 65536.0) + 2.5) * 2.0
    LIIB_pos_3_3V_MonitorLB_L2 = ((LIIB_pos_3_3V_MonitorLB_L1 * 5.0 / 65536.0) + 2.5) * (26.2 / 20.0)
    LIIB_pos_12V_MonitorLB_L2 = ((LIIB_pos_12V_MonitorLB_L1 * 5.0 / 65536.0) + 2.5) * (95.0 / 20.0)
    LIIB_pos_5VB_MonitorLB_L2 = ((LIIB_pos_5VB_MonitorLB_L1 * 5.0 / 65536.0) + 2.5) * 2.0
    LIIB_neg_5VB_MonitorLB_L2 = ((LIIB_neg_5VB_MonitorLB_L1 * 5.0 / 65536.0) + 2.5) * -4.0
    LIIB_pos_15VB_MonitorLB_L2 = ((LIIB_pos_15VB_MonitorLB_L1 * 5.0 / 65536.0) + 2.5) * 6.0
    LIIB_neg_15VB_MonitorLB_L2 = ((LIIB_neg_15VB_MonitorLB_L1 * 5.0 / 65536.0) + 2.5) * -16.0
    LIIB_temperatureMonitor3LB_L2 = ((LIIB_temperatureMonitor3LB_L1 * 5.0 / 65536.0) + 2.5) * 250.0 - 273.0
    LIIB_temperatureMonitor2LB_L2 = ((LIIB_temperatureMonitor2LB_L1 * 5.0 / 65536.0) + 2.5) * 250.0 - 273.0
    LIIB_temperatureMonitor1LB_L2 = ((LIIB_temperatureMonitor1LB_L1 * 5.0 / 65536.0) + 2.5) * 250.0 - 273.0
    LIIB_pos_5VB_CurrentMonitorLB_L2 = ((LIIB_pos_5VB_CurrentMonitorLB_L1 * 5.0 / 65536.0) + 2.5) * 1.0
    LIIB_neg_5VB_CurrentMonitorLB_L2 = ((LIIB_neg_5VB_CurrentMonitorLB_L1 * 5.0 / 65536.0) + 2.5) * 0.2
    LIIB_pos_15VB_CurrentMonitorLB_L2 = ((LIIB_pos_15VB_CurrentMonitorLB_L1 * 5.0 / 65536.0) + 2.5) * 1.0
    LIIB_neg_15VB_CurrentMonitorLB_L2 = ((LIIB_neg_15VB_CurrentMonitorLB_L1 * 5.0 / 65536.0) + 2.5) * 0.2
    LIIB_thermalKnife1VoltageMonitorLB_L2 = ((LIIB_thermalKnife1VoltageMonitorLB_L1 * 5.0 / 65536.0) + 2.5) * (
    114.7 / 14.7)
    LIIB_thermalKnife2VoltageMonitorLB_L2 = ((LIIB_thermalKnife2VoltageMonitorLB_L1 * 5.0 / 65536.0) + 2.5) * (
    114.7 / 14.7)
    if LIIB_thermalKnife1Status_L1 == 1:
        LIIB_thermalKnife1Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife1Status_L1 == 0:
        LIIB_thermalKnife1Status_L2 = 'OPEN'
    if LIIB_thermalKnife2Status_L1 == 1:
        LIIB_thermalKnife2Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife2Status_L1 == 0:
        LIIB_thermalKnife2Status_L2 = 'OPEN'
    if LIIB_thermalKnife3Status_L1 == 1:
        LIIB_thermalKnife3Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife3Status_L1 == 0:
        LIIB_thermalKnife3Status_L2 = 'OPEN'
    if LIIB_thermalKnife4Status_L1 == 1:
        LIIB_thermalKnife4Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife4Status_L1 == 0:
        LIIB_thermalKnife4Status_L2 = 'OPEN'
    if LIIB_tkOverrideToggleStatus_L1 == 1:
        LIIB_tkOverrideToggleStatus_L2 = 'ON'
    elif LIIB_tkOverrideToggleStatus_L1 == 0:
        LIIB_tkOverrideToggleStatus_L2 = 'OFF'

    cur.execute(
        """INSERT INTO subsystem_liib_data (createdAt, updatedAt, orbitElapsedTime, orbitNumber,  packetID, satelliteUTCTime, instrumentLIIB, startWordLIIB_L1, LIIBMode_L1, opMode_L1, pos_5VD_MonitorLB, pos_3_3V_MonitorLB, pos_12V_MonitorLB, pos_5VB_MonitorLB, neg_5VB_MonitorLB, pos_15VB_MonitorLB, neg_15VB_MonitorLB, temperatureMonitor3LB, temperatureMonitor2LB, temperatureMonitor1LB, pos_5VB_CurrentMonitorLB, neg_5VB_CurrentMonitorLB, pos_15VB_CurrentMonitorLB, neg_15VB_CurrentMonitorLB, thermalKnife1VoltageMonitorLB, thermalKnife2VoltageMonitorLB, thermalKnife1Status_L1, thermalKnife2Status_L1, thermalKnife3Status_L1, thermalKnife4Status_L1, tkOverrideToggleStatus_L1, unused, startWordLIIB_L2, LIIBMode_L2, opMode_L2, pos_5VD_Monitor_LB_Volts, pos_3_3V_Monitor_LB_Volts, pos_12V_Monitor_LB_Volts, pos_5VB_MonitorLB_Volts, neg_5VB_MonitorLB_Volts, pos_15VB_MonitorLB_Volts, neg_15VB_MonitorLB_Volts, temperatureMonitor3LB_degC, temperatureMonitor2LB_degC, temperatureMonitor1LB_degC, pos_5VB_CurrentMonitorLB_Volts, neg_5VB_CurrentMonitorLB_Volts, pos_15VB_CurrentMonitorLB_Volts, neg_15VB_CurrentMonitorLB_Volts, thermalKnife1VoltageMonitorLB_Volts, thermalKnife2VoltageMonitorLB_Volts, thermalKnife1Status_L2, thermalKnife2Status_L2, thermalKnife3Status_L2, thermalKnife4Status_L2, tkOverrideToggleStatus_L2) VALUES ("%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (
            createdAt, createdAt, orbitElapsedTime, orbitNumber, packetID, satelliteUTCTime, instrumentLIIB,
            LIIB_startWordLIIB_L1, LIIB_LIIBMode_L1, LIIB_opMode_L1, LIIB_pos_5VD_MonitorLB_L1, LIIB_pos_3_3V_MonitorLB_L1,
            LIIB_pos_12V_MonitorLB_L1, LIIB_pos_5VB_MonitorLB_L1, LIIB_neg_5VB_MonitorLB_L1, LIIB_pos_15VB_MonitorLB_L1,
            LIIB_neg_15VB_MonitorLB_L1, LIIB_temperatureMonitor3LB_L1, LIIB_temperatureMonitor2LB_L1,
            LIIB_temperatureMonitor1LB_L1, LIIB_pos_5VB_CurrentMonitorLB_L1, LIIB_neg_5VB_CurrentMonitorLB_L1,
            LIIB_pos_15VB_CurrentMonitorLB_L1, LIIB_neg_15VB_CurrentMonitorLB_L1, LIIB_thermalKnife1VoltageMonitorLB_L1,
            LIIB_thermalKnife2VoltageMonitorLB_L1, LIIB_thermalKnife1Status_L1, LIIB_thermalKnife2Status_L1,
            LIIB_thermalKnife3Status_L1, LIIB_thermalKnife4Status_L1, LIIB_tkOverrideToggleStatus_L1, unused_L1,
            LIIB_startWordLIIB_L2, LIIB_LIIBMode_L2, LIIB_opMode_L2, LIIB_pos_5VD_MonitorLB_L2, LIIB_pos_3_3V_MonitorLB_L2,
            LIIB_pos_12V_MonitorLB_L2, LIIB_pos_5VB_MonitorLB_L2, LIIB_neg_5VB_MonitorLB_L2, LIIB_pos_15VB_MonitorLB_L2,
            LIIB_neg_15VB_MonitorLB_L2, LIIB_temperatureMonitor3LB_L2, LIIB_temperatureMonitor2LB_L2,
            LIIB_temperatureMonitor1LB_L2, LIIB_pos_5VB_CurrentMonitorLB_L2, LIIB_neg_5VB_CurrentMonitorLB_L2,
            LIIB_pos_15VB_CurrentMonitorLB_L2, LIIB_neg_15VB_CurrentMonitorLB_L2, LIIB_thermalKnife1VoltageMonitorLB_L2,
            LIIB_thermalKnife2VoltageMonitorLB_L2, LIIB_thermalKnife1Status_L2, LIIB_thermalKnife2Status_L2,
            LIIB_thermalKnife3Status_L2, LIIB_thermalKnife4Status_L2, LIIB_tkOverrideToggleStatus_L2))

    '''
    Level 1 - LINAS
    '''

    LINAS_header_L1_Dec = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_header_L1 = hex(LINAS_header_L1_Dec)
    LINAS_filGridGridLow = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    LINAS_filament_OneHalf_L1 = (LINAS_filGridGridLow >> 7) & 0b1 #rs 7 mask 1
    LINAS_gridBias_OnOff_L1 = (LINAS_filGridGridLow >> 6) & 0b1 #rs 7 mask 1
    LINAS_gridBiasSetting_L1 = (LINAS_filGridGridLow >> 2) & 0b1111 #rs 2 mask 4
    LINAS_lowhighFil = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    LINAS_collectorLowRange_L1 = (LINAS_filGridGridLow) & 0b111 #rs 7 mask 1 #Conctanate last bit from previous byte
    LINAS_collectorHighRange_L1 = (LINAS_lowhighFil >> 4) & 0b111 #rs 4 mask 3
    LINAS_filament_OnOff_L1 = (LINAS_lowhighFil) & 0b1111 #rs 0 mask 4
    LINAS_packetCounter_L1 = struct.unpack(short_fmt, f.read(2))[0]
    LINAS_powerError = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L1 = (LINAS_powerError >> 4) & 0b1111 #rs 4 mask 4
    LINAS_errorStatus_Range_TBD_L1 = (LINAS_powerError) & 0b1111 #rs 0 mask 4
    LINAS_watchdogTimeoutCounter_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_gaugeTemp_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_boardTemp_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_pos_12V_Monitor_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_referenceVoltage_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_filamentSupplyCurrent_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_filamentControlVoltage_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_ieReference_4096V_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_gridMonitor_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_igCollectorCurrent_L1 = struct.unpack('>4B', f.read(4))[0]
    LINAS_igEmissionCurrent_L1 = struct.unpack('>4B', f.read(4))[0]
    LINAS_endWordLINAS_L1 = struct.unpack(byte_fmt, f.read(1))[0]


    '''
    Level
    2 - LINAS
    Conver
    to
    ASCII
    '''
    LINAS_header_L2 = str(chr(LINAS_header_L1_Dec))#varchar
    LINAS_filament_OneHalf_L2 = str(chr(LINAS_filament_OneHalf_L1))#varchar
    LINAS_gridBias_OnOff_L2 = str(chr(LINAS_gridBias_OnOff_L1))#varchar
    LINAS_gridBiasSetting_L2 = str(chr(LINAS_gridBiasSetting_L1))#varchar
    LINAS_collectorLowRange_L2 = str(chr(LINAS_collectorLowRange_L1))#varchar
    LINAS_collectorHighRange_L2 = str(chr(LINAS_collectorHighRange_L1))#varchar
    LINAS_filament_OnOff_L2 = str(chr(LINAS_filament_OnOff_L1))#varchar
    #packetCounter_L2 = hex(packetCounter_L1)
    LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L2 = str(chr(LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L1))#varchar
    LINAS_errorStatus_Range_TBD_L2 = str(chr(LINAS_errorStatus_Range_TBD_L1))#varchar
    # watchdogTimeoutCounter_L2 = #in what format?
    # gaugeTemp_L2 = #look up table (see TM Matrix)
    # boardTemp_L2 = #look up table (see TM Matrix)
    LINAS_pos_12V_Monitor_L2 = (LINAS_pos_12V_Monitor_L1)*0.1963
    LINAS_referenceVoltage_L2 = (LINAS_referenceVoltage_L1)*0.01953
    LINAS_filamentSupplyCurrent_L2 = (LINAS_filamentSupplyCurrent_L1)*2.0331/10+5.4691
    LINAS_filamentControlVoltage_L2 = 32 #leave in decimal form
    LINAS_ieReference_4096V_L2 = (LINAS_ieReference_4096V_L1)*0.01953
    LINAS_gridMonitor_L2 = (LINAS_gridMonitor_L1)*0.9848/10 -2.6025
    LINAS_igCollectorCurrent_L2 = (LINAS_igCollectorCurrent_L1-2.85328227*10.0**6.0)/(5.318529932*10.0**6.0)
    LINAS_igEmissionCurrent_L2 =(LINAS_igEmissionCurrent_L1-9.697692934*10.0**5.0)/(9.438607963*10.0**5.0)
    LINAS_endWordLINAS_L2 = LINAS_endWordLINAS_L1#varchar
    #    #pressureReading1_Torr = 2.0 #WHAT CONVERSION HERE?
    #    #pressureReading2_Torr = 2.0 #WHAT CONVERSION HERE?
    #    #pressureReading3_Torr = 2.0 #WHAT CONVERSION HERE?

    cur.execute(
        """INSERT INTO subsystem_linas_data (createdAt,updatedAt,orbitElapsedTime,orbitNumber,packetID,satelliteUTCTime, instrumentLINAS, header_L1,filament_OneHalf_L1,gridBias_OnOff_L1,gridBiasSetting_L1, collectorLowRange_L1,collectorHighRange_L1,filament_OnOff_L1,packetCounter_L1,powerStatus_FilOn_FilSide_GridOn_SAFE_L1,errorStatus_Range_TBD_L1,watchdogTimeoutCounter_L1,gaugeTemp_L1,boardTemp_L1,pos_12V_Monitor_L1,referenceVoltage_L1,filamentSupplyCurrent_L1,filamentControlVoltage_L1,ieReference_4096V_L1,gridMonitor_L1,igCollectorCurrent,igEmissionCurrent,endWordLINAS_L1,header_L2,filament_OneHalf_L2,gridBias_OnOff_L2,gridBiasSetting_L2,collectorLowRange_L2,collectorRightRange_L2,filament_OnOff_L2,powerStatus_FilOn_FilSide_GridOn_SAFE_L2,errorStatus_Range_TBD_L2,pos_12V_Monitor_L2,referenceVoltage_L2,filamentSupplyCurrent_L2,filamentControlVoltage_L2,ieReference_4096V_L2,gridMonitor_L2,collectorCurrent_nA,emissionCurrent_uA,endWordLINAS_L2) VALUES ("%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (
            createdAt, createdAt, orbitElapsedTime, orbitNumber, packetID, satelliteUTCTime, instrumentLINAS,
            LINAS_header_L1_Dec, LINAS_filament_OneHalf_L1, LINAS_gridBias_OnOff_L1, LINAS_gridBiasSetting_L1,
            LINAS_collectorLowRange_L1, LINAS_collectorHighRange_L1, LINAS_filament_OnOff_L1, LINAS_packetCounter_L1,
            LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L1, LINAS_errorStatus_Range_TBD_L1,
            LINAS_watchdogTimeoutCounter_L1,
            LINAS_gaugeTemp_L1, LINAS_boardTemp_L1, LINAS_pos_12V_Monitor_L1, LINAS_referenceVoltage_L1,
            LINAS_filamentSupplyCurrent_L1, LINAS_filamentControlVoltage_L1, LINAS_ieReference_4096V_L1,
            LINAS_gridMonitor_L1, LINAS_igCollectorCurrent_L1, LINAS_igEmissionCurrent_L1, LINAS_endWordLINAS_L1,
            LINAS_header_L2,
            LINAS_filament_OneHalf_L2, LINAS_gridBias_OnOff_L2, LINAS_gridBiasSetting_L2, LINAS_collectorLowRange_L2,
            LINAS_collectorHighRange_L2, LINAS_filament_OnOff_L2, LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L2,
            LINAS_errorStatus_Range_TBD_L2, LINAS_pos_12V_Monitor_L2, LINAS_referenceVoltage_L2,
            LINAS_filamentSupplyCurrent_L2, LINAS_filamentControlVoltage_L2, LINAS_ieReference_4096V_L2,
            LINAS_gridMonitor_L2, LINAS_igCollectorCurrent_L2, LINAS_igEmissionCurrent_L2, LINAS_endWordLINAS_L2))

    '''
    Level 1 - SNeuPI
    '''
    SN_startWordSNeuPI_L1_Dec = struct.unpack(byte_fmt, f.read(1))[0]
    SN_startWordSNeuPI_L1 = hex(SN_startWordSNeuPI_L1_Dec)  # OUTPUT AS HEX DATA
    SN_ZeroHVEmission = struct.unpack(byte_fmt, f.read(1))[0]  # 1 byte to split
    SN_zeroPadding_L1 = (SN_ZeroHVEmission >> 3) & 0b11111  # 0x1f # int("1f", 16.0)
    SN_hv_Status_L1 = (SN_ZeroHVEmission >> 2) & 0b1  # rs 2 mask 1
    SN_emissionMode_L1 = (SN_ZeroHVEmission) & 0b11  # rs 0 mask 2
    SN_pos_3_3V_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_5VD_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_5VB_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_15VB_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_plate1MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_plate2MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_temperatureMonitor1_UpperBoard_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_temperatureMonitorDSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_5V_Converter_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_spaceMonitor2_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_mcp_CurrentSample1_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_tipV1_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_mcp_CurrentSample2_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_tipV2_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_mcp_CurrentSample3_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_tipV3_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_endWordSNeuPI_L1 = struct.unpack(byte_fmt, f.read(1))[0]

    '''
    Level 2 - SNeuPI
    '''

    SN_startWordSNeuPI_L2 = str(chr(SN_startWordSNeuPI_L1_Dec))  # varchar
    SN_zeroPadding_L2 = SN_zeroPadding_L1  # stay as Binary value
    SN_hv_Status_L2 = str(chr(SN_hv_Status_L1))  # varchar
    if SN_hv_Status_L1 == 1:
        SN_hv_Status_L2 = 'ON'
    elif SN_hv_Status_L1 == 0:
        SN_hv_Status_L2 = 'OFF'
    SN_emissionMode_L2 = str(chr(SN_emissionMode_L1))  # varchar
    SN_pos_3_3V_MonitorSN_L2 = (SN_pos_3_3V_MonitorSN_L1 * 5.0 / 65536.0) / (100.0 / 124.0)
    SN_pos_5VD_MonitorSN_L2 = SN_pos_5VD_MonitorSN_L1 * (5.0 / 65536.0) / (100.0 / 124.0)
    SN_pos_5VB_MonitorSN_L2 = SN_pos_5VB_MonitorSN_L1 * (5.0 / 65536.0) / (100.0 / 124.0)
    SN_pos_15VB_MonitorSN_L2 = SN_pos_15VB_MonitorSN_L1 * (5.0 / 65536.0) / (51.1 / 201.1)
    SN_plate1MonitorSN_L2 = SN_plate1MonitorSN_L1 * (5.0 / 65536.0)
    SN_plate2MonitorSN_L2 = SN_plate1MonitorSN_L1 * (5.0 / 65536.0)
    SN_temperatureMonitor1_UpperBoard_L2 = (SN_temperatureMonitor1_UpperBoard_L1 * (5.0 / 65536.0) / 0.004) - 273.0
    SN_temperatureMonitorDSN_L2 = SN_temperatureMonitorDSN_L1 * (5.0 / 65536.0) / 0.004 - 273.0
    SN_pos_5V_Converter_L2 = SN_pos_5V_Converter_L1 * (5.0 / 65536.0) / (100.0 / 124.0)
    # SN_spaceMonitor2_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK
    # SN_mcp_CurrentSample1_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK
    SN_tipV1_L2 = SN_tipV1_L1 * (5.0 / 65536.0) * (-150.0 / 3.0)
    # mcp_CurrentSample2_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK
    SN_tipV2_L2 = SN_tipV2_L1 * (5.0 / 65536.0) * (-150.0 / 3.0)
    # mcp_CurrentSample3_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK
    SN_tipV3_L2 = SN_tipV3_L1 * (5.0 / 65536.0) * (-150.0 / 3.0)
    SN_endWordSNeuPI_L2 = SN_endWordSNeuPI_L1
    # pressureReading1_Torr =  #WHAT CONVERSION HERE?
    # pressureReading2_Torr = #WHAT CONVERSION HERE?
    # pressureReading3_Torr =  #WHAT CONVERSION HERE?

    cur.execute(
        """INSERT INTO subsystem_sneupi_data (createdAt,updatedAt,orbitElapsedTime,orbitNumber,packetID,satelliteUTCTime, instrumentSNeuPI, startWordSNeuPI_L1,zeroPadding_L1,hv_Status_L1,emissionMode_L1,pos_3_3V_MonitorSN,pos_5VD_MonitorSN,pos_5VB_MonitorSN,pos_15VB_MonitorSN,plate1MonitorSN,plate2MonitorSN,temperatureMonitor1_UpperBoard_L1,temperatureMonitorDSN,pos_5V_Converter,spaceMonitor2_L1,mcp_CurrentSample1,tipV1,mcp_CurrentSample2,tipV2,mcp_CurrentSample3,tipV3,endWordSNeuPI_L1,startWordSNeuPI_L2,zeroPadding_L2,hv_Status_L2,emissionMode_L2,pos_3_3V_MonitorSN_Volts,pos_5VD_MonitorSN_Volts,pos_5VB_MonitorSN_Volts,pos_15VB_MonitorSN_Volts,Plate1MonitorSN_Volts,Plate2MonitorSN_Volts,temperatureMonitor1_UpperBoard_L2,temperatureMonitorDSN_DegC,pos_5V_Converter_Volts,tipV1_Volts,tipV2_Volts,tipV3_Volts,endWordSNeuPI_L2) VALUES ("%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (
            createdAt, createdAt, orbitElapsedTime, orbitNumber, packetID, satelliteUTCTime, instrumentSNeuPI,
            SN_startWordSNeuPI_L1_Dec, SN_zeroPadding_L1, SN_hv_Status_L1, SN_emissionMode_L1, SN_pos_3_3V_MonitorSN_L1,
            SN_pos_5VD_MonitorSN_L1, SN_pos_5VB_MonitorSN_L1, SN_pos_15VB_MonitorSN_L1, SN_plate1MonitorSN_L1,
            SN_plate2MonitorSN_L1, SN_temperatureMonitor1_UpperBoard_L1, SN_temperatureMonitorDSN_L1, SN_pos_5V_Converter_L1, SN_spaceMonitor2_L1, SN_mcp_CurrentSample1_L1, SN_tipV1_L1, SN_mcp_CurrentSample2_L1, SN_tipV2_L1, SN_mcp_CurrentSample3_L1, SN_tipV3_L1, SN_endWordSNeuPI_L1, SN_startWordSNeuPI_L2, SN_zeroPadding_L2, SN_hv_Status_L2, SN_emissionMode_L2, SN_pos_3_3V_MonitorSN_L2, SN_pos_5VD_MonitorSN_L2, SN_pos_5VB_MonitorSN_L2, SN_pos_15VB_MonitorSN_L2, SN_plate1MonitorSN_L2, SN_plate2MonitorSN_L2, SN_temperatureMonitor1_UpperBoard_L2, SN_temperatureMonitorDSN_L2, SN_pos_5V_Converter_L2, SN_tipV1_L2, SN_tipV2_L2, SN_tipV3_L2, SN_endWordSNeuPI_L2))

    '''
    Level 1 - RPA
    '''
    RPA_stepSize_L1 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_ptsPerSweep_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    RPA_PtsZeroRG2 = struct.unpack(byte_fmt, f.read(1))[0]  # 1 byte to split
    RPA_zeroPadding_L1 = (RPA_PtsZeroRG2 >> 3) & 0b11111  # 0x1f # int("1f", 16.0)
    RPA_rg2Mode_L1 = (RPA_PtsZeroRG2 >> 2) & 0b1  # rs 2 mask 1
    RPA_sweepMode_rgMode_L1 = (RPA_PtsZeroRG2) & 0b11  # rs 0 mask 2
    RPA_tempMonitor_1RPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_tempMonitor_2RPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_tempMonitor_3RPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_tempMonitor_dbRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_pos_15V_MonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_pos_5V_MonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_pos_3_3_MonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_rg2GridMonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_sgGridMonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample1 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample1 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample2 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample2 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample3 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample3 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample4 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample4 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample5 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample5 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample6 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample6 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample7 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample7 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample8 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample8 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample9 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample9 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample10 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample10 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample11 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample11 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample12 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample12 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample13 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample13 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample14 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample14 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample15 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample15 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample16 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample16 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample17 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample17 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample18 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample18 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample19 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample19 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample20 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample20 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample21 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample21 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample22 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample22 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample23 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample23 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample24 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample24 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample25 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample25 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample26 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample26 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample27 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample27 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample28 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample28 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample29 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample29 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample30 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample30 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample31 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample31 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample32 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample32 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample33 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample33 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample34 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample34 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample35 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample35 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample36 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample36 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample37 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample37 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample38 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample38 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample39 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample39 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample40 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample40 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample41 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample41 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample42 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample42 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample43 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample43 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample44 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample44 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample45 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample45 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample46 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample46 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample47 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample47 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample48 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample48 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample49 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample49 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample50 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample50 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample51 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample51 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample52 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample52 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample53 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample53 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample54 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample54 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample55 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample55 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample56 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample56 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample57 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample57 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample58 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample58 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample59 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample59 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample60 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample60 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample61 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample61 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample62 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample62 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample63 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample63 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample64 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample64 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_endWordRPA = struct.unpack(byte_fmt, f.read(1))[0]

    '''
    Level 2 - RPA, convert
    '''
    RPA_stepSize_L2 = int(RPA_stepSize_L1)  # varchar #check if second parameter changes?
    RPA_ptsPerSweep_L2 = int(RPA_ptsPerSweep_L1)  # varchar
    RPA_zeroPadding_L2 = int(RPA_zeroPadding_L1)  # varchar
    RPA_rg2Mode_L2 = int(RPA_rg2Mode_L1)  # varchar
    RPA_sweepMode_rgMode_L2 = str(chr(RPA_sweepMode_rgMode_L1))  # varchar
    #RPA_tempMonitor_1RPA_degC = (RPA_tempMonitor_1RPA * 5.0 / 65536.0) - 273.0 (database schema has not defined proper datatype)
    #RPA_tempMonitor_2RPA_degC = (RPA_tempMonitor_2RPA * 5.0 / 65536.0) - 273.0
    #RPA_tempMonitor_3RPA_degC = (RPA_tempMonitor_3RPA * 5.0 / 65536.0) - 273.0
    #RPA_tempMonitor_dbRPA_degC = (RPA_tempMonitor_dbRPA * 5.0 / 65536.0) - 273.0
    RPA_pos_15V_MonitorRPA_Volts = ((RPA_pos_15V_MonitorRPA) * 5.0 / 65536.0) * (114.7 / 14.7)
    RPA_pos_5V_MonitorRPA_Volts = (RPA_pos_5V_MonitorRPA * 5.0 / 65536.0) * 2.0
    RPA_pos_3_3_MonitorRPA_Volts = (RPA_pos_3_3_MonitorRPA * 5.0 / 65536.0) * 1.147
    # rg2GridMonitorRPA_Volts #NOT USED
    # sgGridMonitorRPA_Volts #NOT USED

    RPA_currentSample1_Amps = 10.0 ** ((-RPA_currentSample1 - 54335.0) / 11469.0)
    RPA_voltageSample1_Volts = (RPA_voltageSample1 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample2_Amps = 10.0 ** ((-RPA_currentSample2 - 54335.0) / 11469.0)
    RPA_voltageSample2_Volts = (RPA_voltageSample2 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample3_Amps = 10.0 ** ((-RPA_currentSample3 - 54335.0) / 11469.0)
    RPA_voltageSample3_Volts = (RPA_voltageSample3 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample4_Amps = 10.0 ** ((-RPA_currentSample4 - 54335.0) / 11469.0)
    RPA_voltageSample4_Volts = (RPA_voltageSample4 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample5_Amps = 10.0 ** ((-RPA_currentSample5 - 54335.0) / 11469.0)
    RPA_voltageSample5_Volts = (RPA_voltageSample5 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample6_Amps = 10.0 ** ((-RPA_currentSample6 - 54335.0) / 11469.0)
    RPA_voltageSample6_Volts = (RPA_voltageSample6 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample7_Amps = 10.0 ** ((-RPA_currentSample7 - 54335.0) / 11469.0)
    RPA_voltageSample7_Volts = (RPA_voltageSample7 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample8_Amps = 10.0 ** ((-RPA_currentSample8 - 54335.0) / 11469.0)
    RPA_voltageSample8_Volts = (RPA_voltageSample8 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample9_Amps = 10.0 ** ((-RPA_currentSample9 - 54335.0) / 11469.0)
    RPA_voltageSample9_Volts = (RPA_voltageSample9 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample10_Amps = 10.0 ** ((-RPA_currentSample10 - 54335.0) / 11469.0)
    RPA_voltageSample10_Volts = (RPA_voltageSample10 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample11_Amps = 10.0 ** ((-RPA_currentSample11 - 54335.0) / 11469.0)
    RPA_voltageSample11_Volts = (RPA_voltageSample11 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample12_Amps = 10.0 ** ((-RPA_currentSample12 - 54335.0) / 11469.0)
    RPA_voltageSample12_Volts = (RPA_voltageSample12 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample13_Amps = 10.0 ** ((-RPA_currentSample13 - 54335.0) / 11469.0)
    RPA_voltageSample13_Volts = (RPA_voltageSample13 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample14_Amps = 10.0 ** ((-RPA_currentSample14 - 54335.0) / 11469.0)
    RPA_voltageSample14_Volts = (RPA_voltageSample14 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample15_Amps = 10.0 ** ((-RPA_currentSample15 - 54335.0) / 11469.0)
    RPA_voltageSample15_Volts = (RPA_voltageSample15 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample16_Amps = 10.0 ** ((-RPA_currentSample16 - 54335.0) / 11469.0)
    RPA_voltageSample16_Volts = (RPA_voltageSample16 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample17_Amps = 10.0 ** ((-RPA_currentSample17 - 54335.0) / 11469.0)
    RPA_voltageSample17_Volts = (RPA_voltageSample17 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample18_Amps = 10.0 ** ((-RPA_currentSample18 - 54335.0) / 11469.0)
    RPA_voltageSample18_Volts = (RPA_voltageSample18 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample19_Amps = 10.0 ** ((-RPA_currentSample19 - 54335.0) / 11469.0)
    RPA_voltageSample19_Volts = (RPA_voltageSample19 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample20_Amps = 10.0 ** ((-RPA_currentSample20 - 54335.0) / 11469.0)
    RPA_voltageSample20_Volts = (RPA_voltageSample20 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample21_Amps = 10.0 ** ((-RPA_currentSample21 - 54335.0) / 11469.0)
    RPA_voltageSample21_Volts = (RPA_voltageSample21 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample22_Amps = 10.0 ** ((-RPA_currentSample22 - 54335.0) / 11469.0)
    RPA_voltageSample22_Volts = (RPA_voltageSample22 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample23_Amps = 10.0 ** ((-RPA_currentSample23 - 54335.0) / 11469.0)
    RPA_voltageSample23_Volts = (RPA_voltageSample23 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample24_Amps = 10.0 ** ((-RPA_currentSample24 - 54335.0) / 11469.0)
    RPA_voltageSample24_Volts = (RPA_voltageSample24 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample25_Amps = 10.0 ** ((-RPA_currentSample25 - 54335.0) / 11469.0)
    RPA_voltageSample25_Volts = (RPA_voltageSample25 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample26_Amps = 10.0 ** ((-RPA_currentSample26 - 54335.0) / 11469.0)
    RPA_voltageSample26_Volts = (RPA_voltageSample26 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample27_Amps = 10.0 ** ((-RPA_currentSample27 - 54335.0) / 11469.0)
    RPA_voltageSample27_Volts = (RPA_voltageSample27 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample28_Amps = 10.0 ** ((-RPA_currentSample28 - 54335.0) / 11469.0)
    RPA_voltageSample28_Volts = (RPA_voltageSample28 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample29_Amps = 10.0 ** ((-RPA_currentSample29 - 54335.0) / 11469.0)
    RPA_voltageSample29_Volts = (RPA_voltageSample29 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample30_Amps = 10.0 ** ((-RPA_currentSample30 - 54335.0) / 11469.0)
    RPA_voltageSample30_Volts = (RPA_voltageSample30 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample31_Amps = 10.0 ** ((-RPA_currentSample31 - 54335.0) / 11469.0)
    RPA_voltageSample31_Volts = (RPA_voltageSample31 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample32_Amps = 10.0 ** ((-RPA_currentSample32 - 54335.0) / 11469.0)
    RPA_voltageSample32_Volts = (RPA_voltageSample32 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample33_Amps = 10.0 ** ((-RPA_currentSample33 - 54335.0) / 11469.0)
    RPA_voltageSample33_Volts = (RPA_voltageSample33 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample34_Amps = 10.0 ** ((-RPA_currentSample34 - 54335.0) / 11469.0)
    RPA_voltageSample34_Volts = (RPA_voltageSample34 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample35_Amps = 10.0 ** ((-RPA_currentSample35 - 54335.0) / 11469.0)
    RPA_voltageSample35_Volts = (RPA_voltageSample35 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample36_Amps = 10.0 ** ((-RPA_currentSample36 - 54335.0) / 11469.0)
    RPA_voltageSample36_Volts = (RPA_voltageSample36 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample37_Amps = 10.0 ** ((-RPA_currentSample37 - 54335.0) / 11469.0)
    RPA_voltageSample37_Volts = (RPA_voltageSample37 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample38_Amps = 10.0 ** ((-RPA_currentSample38 - 54335.0) / 11469.0)
    RPA_voltageSample38_Volts = (RPA_voltageSample38 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample39_Amps = 10.0 ** ((-RPA_currentSample39 - 54335.0) / 11469.0)
    RPA_voltageSample39_Volts = (RPA_voltageSample39 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample40_Amps = 10.0 ** ((-RPA_currentSample40 - 54335.0) / 11469.0)
    RPA_voltageSample40_Volts = (RPA_voltageSample40 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample41_Amps = 10.0 ** ((-RPA_currentSample41 - 54335.0) / 11469.0)
    RPA_voltageSample41_Volts = (RPA_voltageSample41 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample42_Amps = 10.0 ** ((-RPA_currentSample42 - 54335.0) / 11469.0)
    RPA_voltageSample42_Volts = (RPA_voltageSample42 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample43_Amps = 10.0 ** ((-RPA_currentSample43 - 54335.0) / 11469.0)
    RPA_voltageSample43_Volts = (RPA_voltageSample43 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample44_Amps = 10.0 ** ((-RPA_currentSample44 - 54335.0) / 11469.0)
    RPA_voltageSample44_Volts = (RPA_voltageSample44 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample45_Amps = 10.0 ** ((-RPA_currentSample45 - 54335.0) / 11469.0)
    RPA_voltageSample45_Volts = (RPA_voltageSample45 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample46_Amps = 10.0 ** ((-RPA_currentSample46 - 54335.0) / 11469.0)
    RPA_voltageSample46_Volts = (RPA_voltageSample46 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample47_Amps = 10.0 ** ((-RPA_currentSample47 - 54335.0) / 11469.0)
    RPA_voltageSample47_Volts = (RPA_voltageSample47 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample48_Amps = 10.0 ** ((-RPA_currentSample48 - 54335.0) / 11469.0)
    RPA_voltageSample48_Volts = (RPA_voltageSample48 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample49_Amps = 10.0 ** ((-RPA_currentSample49 - 54335.0) / 11469.0)
    RPA_voltageSample49_Volts = (RPA_voltageSample49 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample50_Amps = 10.0 ** ((-RPA_currentSample50 - 54335.0) / 11469.0)
    RPA_voltageSample50_Volts = (RPA_voltageSample50 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample51_Amps = 10.0 ** ((-RPA_currentSample51 - 54335.0) / 11469.0)
    RPA_voltageSample51_Volts = (RPA_voltageSample51 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample52_Amps = 10.0 ** ((-RPA_currentSample52 - 54335.0) / 11469.0)
    RPA_voltageSample52_Volts = (RPA_voltageSample52 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample53_Amps = 10.0 ** ((-RPA_currentSample53 - 54335.0) / 11469.0)
    RPA_voltageSample53_Volts = (RPA_voltageSample53 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample54_Amps = 10.0 ** ((-RPA_currentSample54 - 54335.0) / 11469.0)
    RPA_voltageSample54_Volts = (RPA_voltageSample54 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample55_Amps = 10.0 ** ((-RPA_currentSample55 - 54335.0) / 11469.0)
    RPA_voltageSample55_Volts = (RPA_voltageSample55 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample56_Amps = 10.0 ** ((-RPA_currentSample56 - 54335.0) / 11469.0)
    RPA_voltageSample56_Volts = (RPA_voltageSample56 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample57_Amps = 10.0 ** ((-RPA_currentSample57 - 54335.0) / 11469.0)
    RPA_voltageSample57_Volts = (RPA_voltageSample57 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample58_Amps = 10.0 ** ((-RPA_currentSample58 - 54335.0) / 11469.0)
    RPA_voltageSample58_Volts = (RPA_voltageSample58 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample59_Amps = 10.0 ** ((-RPA_currentSample59 - 54335.0) / 11469.0)
    RPA_voltageSample59_Volts = (RPA_voltageSample59 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample60_Amps = 10.0 ** ((-RPA_currentSample60 - 54335.0) / 11469.0)
    RPA_voltageSample60_Volts = (RPA_voltageSample60 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample61_Amps = 10.0 ** ((-RPA_currentSample61 - 54335.0) / 11469.0)
    RPA_voltageSample61_Volts = (RPA_voltageSample61 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample62_Amps = 10.0 ** ((-RPA_currentSample62 - 54335.0) / 11469.0)
    RPA_voltageSample62_Volts = (RPA_voltageSample62 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample63_Amps = 10.0 ** ((-RPA_currentSample63 - 54335.0) / 11469.0)
    RPA_voltageSample63_Volts = (RPA_voltageSample63 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_currentSample64_Amps = 10.0 ** ((-RPA_currentSample64 - 54335.0) / 11469.0)
    RPA_voltageSample64_Volts = (RPA_voltageSample64 * 5.0 / 65536.0) * (12.0 / 5.0)
    RPA_endWordRPA_L2 = RPA_endWordRPA

    cur.execute(
        """INSERT INTO subsystem_rpa_data (createdAt,updatedAt,orbitElapsedTime,orbitNumber,packetID,satelliteUTCTime,instrumentRPA,stepSize_L1,ptsPerSweep_L1,zeroPadding_L1,rg2Mode_L1,sweepMode_rgMode_L1,tempMonitor_1RPA,tempMonitor_2RPA,tempMonitor_3RPA,tempMonitor_dbRPA,pos_15V_MonitorRPA,pos_5V_MonitorRPA,pos_3_3V_MonitorRPA,rg2GridMonitorRPA,sgGridMonitorRPA,currentSample1,voltageSample1,currentSample2,voltageSample2,currentSample3,voltageSample3,currentSample4,voltageSample4,currentSample5,voltageSample5,currentSample6,voltageSample6,currentSample7,voltageSample7,currentSample8,voltageSample8,currentSample9,voltageSample9,currentSample10,voltageSample10,currentSample11,voltageSample11,currentSample12,voltageSample12,currentSample13,voltageSample13,currentSample14,voltageSample14,currentSample15,voltageSample15,currentSample16,voltageSample16,currentSample17,voltageSample17,currentSample18,voltageSample18,currentSample19,voltageSample19,currentSample20,voltageSample20, currentSample21,voltageSample21,currentSample22,voltageSample22,currentSample23,voltageSample23,currentSample24,voltageSample24,currentSample25,voltageSample25,currentSample26,voltageSample26,currentSample27,voltageSample27,currentSample28,voltageSample28,currentSample29,voltageSample29,currentSample30,voltageSample30, currentSample31,voltageSample31,currentSample32,voltageSample32,currentSample33,voltageSample33,currentSample34,voltageSample34,currentSample35,voltageSample35,currentSample36,voltageSample36,currentSample37,voltageSample37,currentSample38,voltageSample38,currentSample39,voltageSample39,currentSample40,voltageSample40, currentSample41,voltageSample41,currentSample42,voltageSample42,currentSample43,voltageSample43,currentSample44,voltageSample44,currentSample45,voltageSample45,currentSample46,voltageSample46,currentSample47,voltageSample47,currentSample48,voltageSample48,currentSample49,voltageSample49,currentSample50,voltageSample50,currentSample51,voltageSample51,currentSample52,voltageSample52,currentSample53,voltageSample53,currentSample54,voltageSample54,currentSample55,voltageSample55,currentSample56,voltageSample56,currentSample57,voltageSample57,currentSample58,voltageSample58,currentSample59,voltageSample59,currentSample60,voltageSample60, currentSample61,voltageSample61,currentSample62,voltageSample62,currentSample63,voltageSample63,currentSample64,voltageSample64,endWordRPA,stepSize_L2,ptsPerSweep_L2,zeroPadding_L2,rg2Mode_L2,sweepMode_rgMode_L2,pos_15V_MonitorRPA_Volts,pos_5V_MonitorRPA_Volts,pos3_3V_MonitorRPA_Volts,currentSample1_Amps,voltageSample1_Volts,currentSample2_Amps,voltageSample2_Volts,currentSample3_Amps,voltageSample3_Volts,currentSample4_Amps,voltageSample4_Volts,currentSample5_Amps,voltageSample5_Volts,currentSample6_Amps,voltageSample6_Volts,currentSample7_Amps,voltageSample7_Volts,currentSample8_Amps,voltageSample8_Volts,currentSample9_Amps,voltageSample9_Volts,currentSample10_Amps,voltageSample10_Volts,currentSample11_Amps,voltageSample11_Volts,currentSample12_Amps,voltageSample12_Volts,currentSample13_Amps,voltageSample13_Volts,currentSample14_Amps,voltageSample14_Volts,currentSample15_Amps,voltageSample15_Volts,currentSample16_Amps,voltageSample16_Volts,currentSample17_Amps,voltageSample17_Volts,currentSample18_Amps,voltageSample18_Volts,currentSample19_Amps,voltageSample19_Volts,currentSample20_Amps,voltageSample20_Volts,currentSample21_Amps,voltageSample21_Volts,currentSample22_Amps,voltageSample22_Volts,currentSample23_Amps,voltageSample23_Volts,currentSample24_Amps,voltageSample24_Volts,currentSample25_Amps,voltageSample25_Volts,currentSample26_Amps,voltageSample26_Volts,currentSample27_Amps,voltageSample27_Volts,currentSample28_Amps,voltageSample28_Volts,currentSample29_Amps,voltageSample29_Volts,currentSample30_Amps,voltageSample30_Volts,currentSample31_Amps,voltageSample31_Volts,currentSample32_Amps,voltageSample32_Volts,currentSample33_Amps,voltageSample33_Volts,currentSample34_Amps,voltageSample34_Volts,currentSample35_Amps,voltageSample35_Volts,currentSample36_Amps,voltageSample36_Volts,currentSample37_Amps,voltageSample37_Volts,currentSample38_Amps,voltageSample38_Volts,currentSample39_Amps,voltageSample39_Volts,currentSample40_Amps,voltageSample40_Volts,currentSample41_Amps,voltageSample41_Volts,currentSample42_Amps,voltageSample42_Volts,currentSample43_Amps,voltageSample43_Volts,currentSample44_Amps,voltageSample44_Volts,currentSample45_Amps,voltageSample45_Volts,currentSample46_Amps,voltageSample46_Volts,currentSample47_Amps,voltageSample47_Volts,currentSample48_Amps,voltageSample48_Volts,currentSample49_Amps,voltageSample49_Volts,currentSample50_Amps,voltageSample50_Volts, currentSample51_Amps,voltageSample51_Volts,currentSample52_Amps,voltageSample52_Volts,currentSample53_Amps,voltageSample53_Volts,currentSample54_Amps,voltageSample54_Volts,currentSample55_Amps,voltageSample55_Volts,currentSample56_Amps,voltageSample56_Volts,currentSample57_Amps,voltageSample57_Volts,currentSample58_Amps,voltageSample58_Volts,currentSample59_Amps,voltageSample59_Volts,currentSample60_Amps,voltageSample60_Volts,currentSample61_Amps,voltageSample61_Volts,currentSample62_Amps,voltageSample62_Volts,currentSample63_Amps,voltageSample63_Volts,currentSample64_Amps,voltageSample64_Volts) VALUES ("%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s",  "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")""" % (
            createdAt, updatedAt, orbitElapsedTime, orbitNumber, packetID, satelliteUTCTime, instrumentRPA,
            RPA_stepSize_L1, RPA_ptsPerSweep_L1, RPA_zeroPadding_L1, RPA_rg2Mode_L1, RPA_sweepMode_rgMode_L1,
            RPA_tempMonitor_1RPA, RPA_tempMonitor_2RPA, RPA_tempMonitor_3RPA, RPA_tempMonitor_dbRPA,
            RPA_pos_15V_MonitorRPA, RPA_pos_5V_MonitorRPA, RPA_pos_3_3_MonitorRPA, RPA_rg2GridMonitorRPA,
            RPA_sgGridMonitorRPA, RPA_currentSample1, RPA_voltageSample1, RPA_currentSample2, RPA_voltageSample2,
            RPA_currentSample3, RPA_voltageSample3, RPA_currentSample4, RPA_voltageSample4, RPA_currentSample5,
            RPA_voltageSample5, RPA_currentSample6, RPA_voltageSample6, RPA_currentSample7, RPA_voltageSample7,
            RPA_currentSample8, RPA_voltageSample8, RPA_currentSample9, RPA_voltageSample9, RPA_currentSample10,
            RPA_voltageSample10, RPA_currentSample11, RPA_voltageSample11, RPA_currentSample12, RPA_voltageSample12,
            RPA_currentSample13, RPA_voltageSample13, RPA_currentSample14, RPA_voltageSample14, RPA_currentSample15,
            RPA_voltageSample15, RPA_currentSample16, RPA_voltageSample16, RPA_currentSample17, RPA_voltageSample17,
            RPA_currentSample18, RPA_voltageSample18, RPA_currentSample19, RPA_voltageSample19, RPA_currentSample20,
            RPA_voltageSample20, RPA_currentSample21, RPA_voltageSample21, RPA_currentSample22, RPA_voltageSample22,
            RPA_currentSample23, RPA_voltageSample23, RPA_currentSample24, RPA_voltageSample24, RPA_currentSample25,
            RPA_voltageSample25, RPA_currentSample26, RPA_voltageSample26, RPA_currentSample27, RPA_voltageSample27,
            RPA_currentSample28, RPA_voltageSample28, RPA_currentSample29, RPA_voltageSample29, RPA_currentSample30,
            RPA_voltageSample30, RPA_currentSample31, RPA_voltageSample31, RPA_currentSample32, RPA_voltageSample32,
            RPA_currentSample33, RPA_voltageSample33, RPA_currentSample34, RPA_voltageSample34, RPA_currentSample35,
            RPA_voltageSample35, RPA_currentSample36, RPA_voltageSample36, RPA_currentSample37, RPA_voltageSample37,
            RPA_currentSample38, RPA_voltageSample38, RPA_currentSample39, RPA_voltageSample39, RPA_currentSample40,RPA_voltageSample40,
            RPA_currentSample41, RPA_voltageSample42, RPA_currentSample42, RPA_voltageSample42,RPA_currentSample43, RPA_voltageSample43, RPA_currentSample44, RPA_voltageSample44, RPA_currentSample45,
            RPA_voltageSample45, RPA_currentSample46, RPA_voltageSample46, RPA_currentSample47, RPA_voltageSample47,
            RPA_currentSample48, RPA_voltageSample48, RPA_currentSample49, RPA_voltageSample49, RPA_currentSample50,
            RPA_voltageSample50,RPA_currentSample51, RPA_voltageSample51, RPA_currentSample52, RPA_voltageSample52,
            RPA_currentSample53, RPA_voltageSample53, RPA_currentSample54, RPA_voltageSample54, RPA_currentSample55,
            RPA_voltageSample55, RPA_currentSample56, RPA_voltageSample56, RPA_currentSample57, RPA_voltageSample57,
            RPA_currentSample58, RPA_voltageSample58, RPA_currentSample59, RPA_voltageSample59, RPA_currentSample60,
            RPA_voltageSample60, RPA_currentSample61, RPA_voltageSample61, RPA_currentSample62, RPA_voltageSample62,
            RPA_currentSample63, RPA_voltageSample63, RPA_currentSample64, RPA_voltageSample64, RPA_endWordRPA,
            RPA_stepSize_L2, RPA_ptsPerSweep_L2, RPA_zeroPadding_L2, RPA_rg2Mode_L2, RPA_sweepMode_rgMode_L2,
            RPA_pos_15V_MonitorRPA_Volts, RPA_pos_5V_MonitorRPA_Volts, RPA_pos_3_3_MonitorRPA_Volts,
            RPA_currentSample1_Amps, RPA_voltageSample1_Volts, RPA_currentSample2_Amps, RPA_voltageSample2_Volts,
            RPA_currentSample3_Amps, RPA_voltageSample3_Volts, RPA_currentSample4_Amps, RPA_voltageSample4_Volts,
            RPA_currentSample5_Amps, RPA_voltageSample5_Volts, RPA_currentSample6_Amps, RPA_voltageSample6_Volts,
            RPA_currentSample7_Amps, RPA_voltageSample7_Volts, RPA_currentSample8_Amps, RPA_voltageSample8_Volts,
            RPA_currentSample9_Amps, RPA_voltageSample9_Volts, RPA_currentSample10_Amps, RPA_voltageSample10_Volts,
            RPA_currentSample11_Amps, RPA_voltageSample11_Volts, RPA_currentSample12_Amps, RPA_voltageSample12_Volts,
            RPA_currentSample13_Amps, RPA_voltageSample13_Volts, RPA_currentSample14_Amps, RPA_voltageSample14_Volts,
            RPA_currentSample15_Amps, RPA_voltageSample15_Volts, RPA_currentSample16_Amps, RPA_voltageSample16_Volts,
            RPA_currentSample17_Amps, RPA_voltageSample17_Volts, RPA_currentSample18_Amps, RPA_voltageSample18_Volts,
            RPA_currentSample19_Amps, RPA_voltageSample19_Volts, RPA_currentSample20_Amps, RPA_voltageSample20_Volts,
            RPA_currentSample21_Amps, RPA_voltageSample21_Volts, RPA_currentSample22_Amps, RPA_voltageSample22_Volts,
            RPA_currentSample23_Amps, RPA_voltageSample23_Volts, RPA_currentSample24_Amps, RPA_voltageSample24_Volts,
            RPA_currentSample25_Amps, RPA_voltageSample25_Volts, RPA_currentSample26_Amps, RPA_voltageSample26_Volts,
            RPA_currentSample27_Amps, RPA_voltageSample27_Volts, RPA_currentSample28_Amps, RPA_voltageSample28_Volts,
            RPA_currentSample29_Amps, RPA_voltageSample29_Volts, RPA_currentSample30_Amps, RPA_voltageSample30_Volts,
            RPA_currentSample31_Amps, RPA_voltageSample31_Volts, RPA_currentSample32_Amps, RPA_voltageSample32_Volts,
            RPA_currentSample33_Amps, RPA_voltageSample33_Volts, RPA_currentSample34_Amps, RPA_voltageSample34_Volts,
            RPA_currentSample35_Amps, RPA_voltageSample35_Volts, RPA_currentSample36_Amps, RPA_voltageSample36_Volts,
            RPA_currentSample37_Amps, RPA_voltageSample37_Volts, RPA_currentSample38_Amps, RPA_voltageSample38_Volts,
            RPA_currentSample39_Amps, RPA_voltageSample39_Volts, RPA_currentSample40_Amps, RPA_voltageSample40_Volts,
            RPA_currentSample41_Amps, RPA_voltageSample41_Volts, RPA_currentSample42_Amps, RPA_voltageSample42_Volts,
            RPA_currentSample43_Amps, RPA_voltageSample43_Volts, RPA_currentSample44_Amps, RPA_voltageSample44_Volts,
            RPA_currentSample45_Amps, RPA_voltageSample45_Volts, RPA_currentSample46_Amps, RPA_voltageSample46_Volts,
            RPA_currentSample47_Amps, RPA_voltageSample47_Volts, RPA_currentSample48_Amps, RPA_voltageSample48_Volts,
            RPA_currentSample49_Amps, RPA_voltageSample49_Volts, RPA_currentSample50_Amps,RPA_voltageSample50_Volts,
            RPA_currentSample51_Amps, RPA_voltageSample51_Volts, RPA_currentSample52_Amps, RPA_voltageSample52_Volts,
            RPA_currentSample53_Amps, RPA_voltageSample53_Volts, RPA_currentSample54_Amps, RPA_voltageSample54_Volts,
            RPA_currentSample55_Amps, RPA_voltageSample55_Volts, RPA_currentSample56_Amps, RPA_voltageSample56_Volts,
            RPA_currentSample57_Amps, RPA_voltageSample57_Volts, RPA_currentSample58_Amps, RPA_voltageSample58_Volts,
            RPA_currentSample59_Amps, RPA_voltageSample59_Volts, RPA_currentSample60_Amps, RPA_voltageSample60_Volts,
            RPA_currentSample61_Amps, RPA_voltageSample61_Volts, RPA_currentSample62_Amps, RPA_voltageSample62_Volts,
            RPA_currentSample63_Amps, RPA_voltageSample63_Volts, RPA_currentSample64_Amps, RPA_voltageSample64_Volts))

    conn.commit()

insert_one_record(cmd, resp, time, conn)

