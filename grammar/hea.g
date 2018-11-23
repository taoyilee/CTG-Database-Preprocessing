%import common.SIGNED_NUMBER
%import common.NUMBER
%import common.NEWLINE
%import common.WS
%import common.LETTER
%import common.WORD
%import common.DIGIT
%ignore WS

start: record lines+
record: record_name number_of_signals sampling_frequency?
?lines: signal_spec | addi_block

RECORD_NAME: (LETTER|DIGIT|"_")+
record_name: RECORD_NAME
number_of_signals: NUMBER
sampling_frequency: NUMBER counter_frequency? number_of_samples?
counter_frequency: "/" NUMBER base_counter_value?
base_counter_value: "(" NUMBER ")"
number_of_samples: NUMBER base_time?
base_time: DIGIT DIGIT ":" DIGIT DIGIT ":" DIGIT DIGIT base_date?
base_date: DIGIT DIGIT "/" DIGIT DIGIT "/" DIGIT DIGIT DIGIT DIGIT

FILE_BASE_NAME: RECORD_NAME
dat_name: RECORD_NAME ".dat"
?file_name: dat_name
!signal_format: "8" | "16" | "24" | "32" | "61" | "80" | "160" | "212" | "310" | "311"
samples_per_frame: NUMBER "x"
skew: NUMBER ":"
byte_offset: NUMBER "+"
adc_gain: NUMBER baseline_adc? adc_units? adc_resol?
baseline_adc: "(" NUMBER ")"
adc_units: "/" WORD
adc_resol: NUMBER adc_zero?
adc_zero: NUMBER adc_init_val?
adc_init_val: NUMBER adc_checksum?
adc_checksum: NUMBER adc_block_size?
adc_block_size: NUMBER
!signal_description: "FHR" | "UC"


signal_spec: file_name signal_format samples_per_frame? skew? byte_offset? adc_gain? signal_description?
?addi_block: "#----- Additional parameters for record" record_name addi_subblock+
?addi_subblock: fetus_block | delivery_block | maternal_block | outcome_block | signal_block | neonatal_oc_block
fetus_block: "#-- Fetus/Neonate descriptors" field_comment+
outcome_block: "#-- Outcome measures" field_comment+
signal_block: "#-- Signal information" field_comment+
neonatal_oc_block: "#-- !NotReadyYet! Neonatology outcome measures !NotReadyYet!" field_comment+
delivery_block: "#-- Delivery descriptors" field_comment+
maternal_block: "#-- Maternal (risk-)factors" field_comment+
comment: /#[^\n]*/
lab_meas: lab_meas_field lab_meas_number
LAB_FIELD_NAME: (DIGIT|LETTER|"("|")"|"/"|".")+
lab_meas_field: LAB_FIELD_NAME ~ 1..2
lab_meas_number: SIGNED_NUMBER
?field_comment: "#" lab_meas