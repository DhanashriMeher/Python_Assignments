import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def studentperdata():
    df = pd.read_csv("student-mat.csv" , sep =";")

    features = df[['G1','G2','G3','studytime','failures','absences']]

    scaler =StandardScaler()
    model = scaler.fit_transform(features)

    Kmeans = KMeans(n_clusters=3,random_state= 42)
    df['Cluster'] = Kmeans.fit_predict(model)

    cluster_summary = df.groupby('Cluster')[['G1','G2','G3','studytime','failures','absences']].mean()
    print("Cluster Summary:")
    print(cluster_summary)

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['G3'], y=df['studytime'], hue=df['Cluster'], palette='viridis')
    plt.title("Student Clusters based on Academic Performance")
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.show()

    cluster_label_map = {
    0: 'Top Performers',
    1: 'Average Students',
    2: 'Struggling Students'
    }
    df['PerformanceGroup'] = df['Cluster'].map(cluster_label_map)
    
def main() :
    studentperdata()

if __name__ =="__main__":
    main()




