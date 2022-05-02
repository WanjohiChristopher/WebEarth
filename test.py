from sklearn.preprocessing import MiniMaxScaler,StandardScaler


def feature_norm(train,test):
    scaler = MinMaxScaler()

    normalized_train = scaler.fit_transform(train)
    normalized_test= scaler.fit_transform(test)
    