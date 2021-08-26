import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [ [0.2, 0.8, -0.2, 0.3],
            [0.4, 0.3, -0.4, 0.4],
            [0.13, 0.15, -0.5, 0.5]]
biases = [2, 3, 0.5]

#Output of current layer
layer_outputs = []

#For each neuron
for neuron_weights, neuron_biases in zip(weights, biases):
    #Zeroed output of given neuron
    neuron_output = 0
    #For each input and weight into the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        #Multiply the input by associated weight
        # and add to the neuron's output variable
        neuron_output += n_input * weight
    #Add the bias
    neuron_output += neuron_biases

    #Put the result into layer's output list
    layer_outputs.append(neuron_output)

print(layer_outputs)