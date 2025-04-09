from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.h(0)
qc.h(0)
qc.measure(0, 0)

sampler = StatevectorSampler()
job = sampler.run([qc], shots=1000)
result = job.result()
pub_result = result[0]
counts = pub_result.data.c

print(counts.get_counts())