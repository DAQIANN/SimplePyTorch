import numpy as np

N, D_in, H, D_out = 64, 1000, 100, 10
#N:batch size, D_in:input dim, H:hidden dim, D_out:output dim

#Random input and random output
x = np.random.randn(N, D_in)
y = np.random.randn(N, D_out)

#initializing weights random
w1 = np.random.randn(D_in, H)
w2 = np.random.randn(H, D_out)

learning_rate = 1e-6
for t in range(500):
    #Forward pass: compute predicted y
    h = x.dot(w1)
    h_relu = np.maximum(h, 0)
    y_pred = h_relu.dot(w2)

    #Compute and print loss
    loss = np.square(y_pred - y)
    print(t, loss)

    #Backprop to compute gradients of w1 and w2 with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.T.dot(grad_y_pred)
    grad_h_relu = grad_y_pred.dot(w2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)
