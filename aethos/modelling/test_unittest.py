import os
import shutil
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs

from aethos import Classification, Regression, Unsupervised, Analysis


class TestModelling(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):

        models_path = str(Path.home()) + "/.aethos/models/"
        projects_path = str(Path.home()) + "/.aethos/projects/"

        if os.path.exists(models_path):
            shutil.rmtree(models_path)

        if os.path.exists(projects_path):
            shutil.rmtree(projects_path)

    def test_text_gensim_summarize(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        model.summarize_gensim("data", ratio=0.5, run=True)
        validate = model["data_summarized"] is not None

        self.assertTrue(validate)

    def test_text_view_gensim_summarize(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        m = model.summarize_gensim("data", ratio=0.5, run=True)
        m.view("data", "data_summarized")

        self.assertTrue(True)

    def test_text_gensim_keywords(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        model.extract_keywords_gensim("data", ratio=0.5, run=True)
        validate = model.data_extracted_keywords is not None

        self.assertTrue(validate)

    def test_text_gensim_w2v(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        model.Word2Vec("data", prep=True, run=True, min_count=1)
        validate = model.w2v is not None

        self.assertTrue(validate)

    def test_text_gensim_lda(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])
        data["prep"] = pd.Series([text.split() for text in text_data])

        model = Unsupervised(x_train=data)
        model.LDA("prep")
        validate = model.lda is not None

        self.assertTrue(validate)

    def test_text_gensim_prep_lda(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        model.LDA("data", prep=True)
        validate = model.lda is not None

        self.assertTrue(validate)

    def test_text_view_topics(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])
        data["prep"] = pd.Series([text.split() for text in text_data])

        model = Unsupervised(x_train=data)
        l = model.LDA("prep")
        l.view_topics()
        l.view_topic(1)

        self.assertTrue(True)

    def test_text_model_perplexity(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])
        data["prep"] = pd.Series([text.split() for text in text_data])

        model = Unsupervised(x_train=data)
        l = model.LDA("prep")
        l.model_perplexity()

        self.assertTrue(True)

    def test_text_coherence_score(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])
        data["prep"] = pd.Series([text.split() for text in text_data])

        model = Unsupervised(x_train=data)
        l = model.LDA("prep")
        l.coherence_score("prep")

        self.assertTrue(True)

    def test_text_w2vprep(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])
        data["prep"] = pd.Series([text.split() for text in text_data])

        model = Unsupervised(x_train=data)
        model.Word2Vec("prep", run=True, min_count=1)
        validate = model.w2v is not None

        self.assertTrue(validate)

    def test_text_d2v(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        model.Doc2Vec("data", prep=True, run=True, min_count=1)
        validate = model.d2v is not None

        self.assertTrue(validate)

    def test_text_d2vprep(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])
        data["prep"] = pd.Series([text.split() for text in text_data])

        model = Unsupervised(x_train=data)
        model.Doc2Vec("prep", run=True, min_count=1)
        validate = model.d2v is not None

        self.assertTrue(validate)

    def test_model_getattr(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        model.extract_keywords_gensim("data", ratio=0.5, model_name="model1", run=True)
        validate = model.model1 is not None

        self.assertTrue(validate)

    def test_model_addtoqueue(self):

        text_data = [
            "Hi my name is aethos. Please split me.",
            "This function is going to split by sentence. Automation is great.",
        ]

        data = pd.DataFrame(data=text_data, columns=["data"])

        model = Unsupervised(x_train=data)
        model.extract_keywords_gensim("data", ratio=0.5, model_name="model1", run=False)
        model.summarize_gensim("data", ratio=0.5, run=False)
        validate = len(model._queued_models)

        self.assertEqual(validate, 2)

    def test_model_kmeans(self):

        data, _ = make_blobs(n_samples=1000, n_features=12, centers=8, random_state=42)
        data = pd.DataFrame(data=data)

        model = Unsupervised(x_train=data,)
        model.KMeans(n_clusters=3, random_state=0, run=True)
        validate = model.km is not None

        self.assertTrue(validate)

    def test_model_kmeans_nok(self):

        data, _ = make_blobs(n_samples=1000, n_features=12, centers=8, random_state=42)
        data = pd.DataFrame(data=data)

        model = Unsupervised(x_train=data,)
        model.KMeans(random_state=0, run=True)
        validate = model.km is not None

        self.assertTrue(validate)

    def test_model_dbscan(self):

        data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=["col1", "col2"])

        model = Unsupervised(x_train=data,)
        model.DBScan(eps=3, min_samples=2, run=True)
        validate = model.dbs is not None

        self.assertTrue(validate)

    def test_model_cluster_filter(self):

        data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=["col1", "col2"])

        model = Unsupervised(x_train=data,)
        model = model.DBScan(eps=3, min_samples=2, run=True)
        filtered = model.filter_cluster(0)
        validate = all(filtered.predicted == 0)

        self.assertTrue(validate)

    def test_model_defaultgridsearch(self):

        data = [
            [1, 2, 1],
            [2, 2, 1],
            [2, 3, 1],
            [8, 7, 0],
            [8, 8, 0],
            [25, 80, 0],
            [1, 2, 1],
            [3, 2, 0],
            [1, 2, 1],
        ]

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3",)

        gridsearch_params = {"C": [0.2, 1]}
        model.LogisticRegression(
            gridsearch=gridsearch_params, cv_type="kfold", run=True
        )

        self.assertTrue(True)

    def test_model_logisticregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        validate = model.log_reg.y_pred is not None

        self.assertTrue(validate)

    def test_model_confusionmatrix(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3",)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.confusion_matrix()

        self.assertTrue(True)

    def test_model_all_score_metrics(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3",)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.metrics()

        self.assertTrue(True)

    def test_model_report_classificationreport(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3",)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.classification_report()

        self.assertTrue(True)

    def test_model_report_modelweights(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3",)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.model_weights()

        self.assertTrue(True)

    def test_plot_roccurve(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.roc_curve()

        self.assertTrue(True)

    def test_decision_plot(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.decision_plot()

        self.assertTrue(True)

    def test_decision_plot_all(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.decision_plot(num_samples="all")

        self.assertTrue(True)

    def test_decision_plot_sameaxis(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        r = model.log_reg.decision_plot(sample_no=1)
        model.log_reg.decision_plot(
            sample_no=2, feature_order=r.feature_idx, xlim=r.xlim
        )

        self.assertTrue(True)

    def test_decision_plot_misclassified(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.decision_plot(0.75, highlight_misclassified=True)

        self.assertTrue(True)

    def test_force_plot(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.force_plot()

        self.assertTrue(True)

    def test_force_plot_misclassified(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.6)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.force_plot(misclassified=True)

        self.assertTrue(True)

    def test_get_misclassified(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.shap_get_misclassified_index()

        self.assertTrue(True)

    def test_summaryplot(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.summary_plot()

        self.assertTrue(True)

    def test_dependence_plot(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5)
        model.LogisticRegression(random_state=2, penalty="l2", run=True)
        model.log_reg.dependence_plot("col1")

        self.assertTrue(True)

    def test_local_multiprocessing(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l1", run=False
        )
        model.LogisticRegression(
            gridsearch={"C": [0.1, 0.2]},
            random_state=2,
            penalty="l2",
            model_name="l2",
            run=False,
        )
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l3", run=False
        )

        model.run_models()

        self.assertTrue(len(model._models) == 3 and len(model._queued_models) == 0)

    def test_local_seriesprocessing(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l1", run=True
        )
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l2", run=True
        )
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l3", run=True
        )

        model.run_models(method="series")

        self.assertTrue(len(model._models) == 3 and len(model._queued_models) == 0)

    def test_interpretmodel_behaviour_all(self):

        train_data = np.random.random_sample(size=(1000, 2))
        label_data = np.random.randint(0, 2, size=(1000, 1))

        data = pd.DataFrame(data=train_data, columns=["col1", "col2"])
        data["col3"] = label_data

        model = Classification(x_train=data, target="col3", test_split_percentage=0.2)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model_behavior(show=False)

        self.assertTrue(True)

    def test_interpretmodel_behaviour_dependence(self):

        data = np.random.randint(0, 2, size=(500, 3))
        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.4)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model_behavior(method="dependence", show=False)

        self.assertTrue(True)

    def test_interpretmodel_predictions_all(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.6)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model_predictions(show=False)

        self.assertTrue(True)

    def test_interpretmodel_predictions_lime(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.6)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model_predictions(method="lime", show=False)

        self.assertTrue(True)

    def test_interpretmodel_performance_all(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.6)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model_performance(show=False)

        self.assertTrue(True)

    def test_interpretmodel_performance_roc(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.6)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model_performance(method="ROC", show=False)

        self.assertTrue(True)

    def test_interpret_model(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.4)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model(show=False)

        self.assertTrue(True)

    def test_interpret_model_prerun(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.4)
        model.LogisticRegression(random_state=2, run=True)
        model.log_reg.interpret_model_performance(method="ROC", show=False)
        model.log_reg.interpret_model(show=False)

        self.assertTrue(True)

    def test_compareclsmodels(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l1", run=True
        )
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l2", run=True
        )
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l3", run=True
        )

        model.run_models(method="series")
        model.compare_models()

        self.assertTrue(True)

    def test_compareregmodels(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3", test_split_percentage=0.5,)
        model.LinearRegression(model_name="l1", run=True)
        model.LinearRegression(model_name="l2", run=True)
        model.LinearRegression(model_name="l3", run=True)

        model.run_models(method="series")
        model.compare_models()

        self.assertTrue(True)

    def test_cv(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])
        model = Regression(x_train=data, target="col3", test_split_percentage=0.2)
        m = model.LinearRegression()
        m.cross_validate()

        self.assertTrue(True)

    def test_stratified_cv(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])
        model = Classification(x_train=data, target="col3", test_split_percentage=0.2)
        cv_values = model.LogisticRegression(run=True)
        cv_values.cross_validate(cv_type="strat-kfold", n_splits=10)

        self.assertTrue(True)

    def test_del_model(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])
        model = Classification(x_train=data, target="col3", test_split_percentage=0.2)
        model.LogisticRegression(random_state=2, run=True)
        model.delete_model("log_reg")

        self.assertTrue(len(model._models) == 0)

    def test_model_ridgeclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.RidgeClassification(random_state=2, run=True)
        validate = model.ridge_cls is not None

        self.assertTrue(validate)

    def test_model_sgdclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.SGDClassification(random_state=2, run=True)
        validate = model.sgd_cls is not None

        self.assertTrue(validate)

    def test_model_adaclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.ADABoostClassification(random_state=2, run=True)
        validate = model.ada_cls is not None

        self.assertTrue(validate)

    def test_model_bagclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.BaggingClassification(random_state=2, run=True)
        validate = model.bag_cls is not None

        self.assertTrue(validate)

    def test_model_boostingclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.GradientBoostingClassification(random_state=2, run=True)
        validate = model.grad_cls is not None

        self.assertTrue(validate)

    def test_model_isoforest(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Unsupervised(x_train=data)
        model.IsolationForest(random_state=2, run=True)
        validate = model.iso_forest is not None

        self.assertTrue(validate)

    def test_model_oneclasssvm(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Unsupervised(x_train=data)
        model.OneClassSVM(run=True)
        validate = model.ocsvm is not None

        self.assertTrue(validate)

    def test_model_rfclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.RandomForestClassification(random_state=2, run=True)
        validate = model.rf_cls is not None

        self.assertTrue(validate)

    def test_model_view_rfclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.RandomForestClassification(random_state=2, run=True)
        validate = model.rf_cls.view_tree()

        self.assertTrue(True)

    def test_model_bernoulli(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.BernoulliClassification(run=True)
        validate = model.bern is not None

        self.assertTrue(validate)

    def test_model_gaussian(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.GaussianClassification(run=True)
        validate = model.gauss is not None

        self.assertTrue(validate)

    def test_model_multinomial(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.MultinomialClassification(run=True)

        validate = model.multi is not None

        self.assertTrue(validate)

    def test_model_dtclassifier(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.DecisionTreeClassification(random_state=2, run=True)
        validate = model.dt_cls is not None

        self.assertTrue(validate)

    def test_model_linearsvc(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.LinearSVC(random_state=2, run=True)
        validate = model.linsvc is not None

        self.assertTrue(validate)

    def test_model_svc(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.SVC(random_state=2, run=True)
        validate = model.svc_cls is not None

        self.assertTrue(validate)

    def test_model_bayesianridge(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.BayesianRidgeRegression(run=True)
        validate = model.bayridge_reg is not None

        self.assertTrue(validate)

    def test_model_elasticnet(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.ElasticnetRegression(random_state=2, run=True)
        validate = model.elastic is not None

        self.assertTrue(validate)

    def test_model_lasso(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.LassoRegression(random_state=2, run=True)
        validate = model.lasso is not None

        self.assertTrue(validate)

    def test_model_linreg(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.LinearRegression()
        validate = model.lin_reg is not None

        self.assertTrue(validate)

    def test_model_ridgeregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.RidgeRegression(random_state=2, run=True)
        validate = model.ridge_reg is not None

        self.assertTrue(validate)

    def test_model_sgdregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.SGDRegression(random_state=2, run=True)
        validate = model.sgd_reg is not None

        self.assertTrue(validate)

    def test_model_adaregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.ADABoostRegression(random_state=2, run=True)
        validate = model.ada_reg is not None

        self.assertTrue(validate)

    def test_model_bgregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.BaggingRegression(random_state=2, run=True)
        validate = model.bag_reg is not None

        self.assertTrue(validate)

    def test_model_gbregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.GradientBoostingRegression(random_state=2, run=True)
        validate = model.grad_reg is not None

        self.assertTrue(validate)

    def test_model_rfregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.RandomForestRegression(random_state=2, run=True)
        validate = model.rf_reg is not None

        self.assertTrue(validate)

    def test_model_dtregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.DecisionTreeRegression(random_state=2, run=True)
        validate = model.dt_reg is not None

        self.assertTrue(validate)

    def test_model_view_dtregression(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.DecisionTreeRegression(random_state=2, run=True)
        validate = model.dt_reg.view_tree()

        self.assertTrue(True)

    def test_model_linearsvr(self):

        data = np.random.rand(500, 3)

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.LinearSVR(random_state=2, run=True)
        validate = model.linsvr is not None

        self.assertTrue(validate)

    def test_model_view_linearsvr(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.LinearSVR(random_state=2, run=True)

        self.assertRaises(NotImplementedError, model.linsvr.view_tree)

    def test_model_svr(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.SVR(run=True)
        validate = model.svr_reg is not None

        self.assertTrue(validate)

    def test_model_xgbc(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.XGBoostClassification(run=True)
        validate = model.xgb_cls is not None

        self.assertTrue(validate)

    def test_model_view_xgbc(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.XGBoostClassification(run=True)
        validate = model.xgb_cls.view_tree()

        self.assertTrue(True)

    def test_model_xgbr(self):

        data = [
            [1, 2, 0.5],
            [3, 10, 0.2],
            [2, 5, 0.1],
            [5, 6, 1.2],
            [7, 2, 1.5],
            [10, 5, 1.2],
        ]

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.XGBoostRegression(run=True)
        validate = model.xgb_reg is not None

        self.assertTrue(validate)

    def test_model_lgbc(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.LightGBMClassification(run=True)
        validate = model.lgbm_cls is not None

        self.assertTrue(validate)

    def test_model_lgbr(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.LightGBMRegression(run=True)
        validate = model.lgbm_reg is not None

        self.assertTrue(True)

    def test_model_view_lgbr(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.LightGBMRegression(run=True)
        model.lgbm_reg.view_tree()

        self.assertTrue(True)

    def test_model_agglom(self):

        data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=["col1", "col2"])

        model = Unsupervised(x_train=data,)
        model.AgglomerativeClustering(n_clusters=2, run=True)
        validate = model.agglom is not None

        self.assertTrue(validate)

    def test_model_meanshift(self):

        data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=["col1", "col2"])

        model = Unsupervised(x_train=data,)
        model.MeanShift(run=True)
        validate = model.mshift is not None

        self.assertTrue(validate)

    def test_model_gaussianmixture(self):

        data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=["col1", "col2"])

        model = Unsupervised(x_train=data,)
        model.GaussianMixtureClustering(run=True)
        validate = model.gm_cluster is not None

        self.assertTrue(validate)

    def test_plot_clusters2d(self):

        data = [[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]]

        data = pd.DataFrame(data=data, columns=["col1", "col2"])

        model = Unsupervised(x_train=data,)
        model.KMeans(n_clusters=3, random_state=0, run=True)
        model.km.plot_clusters()

        self.assertTrue(True)

    def test_plot_clusters3d(self):

        data = [[1, 2, 3], [2, 2, 3], [2, 3, 4], [8, 7, 5], [8, 8, 5], [25, 80, 4]]

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Unsupervised(x_train=data,)
        model.KMeans(n_clusters=3, random_state=0, run=True)
        model.km.plot_clusters(dim=3)

        self.assertTrue(True)

    def test_ytrain_split(self):

        data = [
            [1, 0, 0],
            [0, 2, 3],
            [0, 3, 4],
            [1, 2, 3],
            [1, 0, 0],
            [0, 2, 3],
            [0, 3, 4],
            [1, 2, 3],
        ]
        columns = ["col1", "col2", "col3"]
        data = pd.DataFrame(data, columns=columns)

        base = Classification(x_train=data, target="col3", test_split_percentage=0.5,)

        validate = (
            base.x_train[base.target].tolist() == base.y_train.tolist()
            and len(base.y_train) == 4
        )

        self.assertTrue(validate)

    def test_ytest_split(self):

        data = [
            [1, 0, 0],
            [0, 2, 3],
            [0, 3, 4],
            [1, 2, 3],
            [1, 0, 0],
            [0, 2, 3],
            [0, 3, 4],
            [1, 2, 3],
        ]
        columns = ["col1", "col2", "col3"]
        data = pd.DataFrame(data, columns=columns)

        base = Classification(x_train=data, target="col3", test_split_percentage=0.5,)

        validate = (
            base.x_test[base.target].tolist() == base.y_test.tolist()
            and len(base.y_test) == 4
        )

        self.assertTrue(validate)

    def test_pickle_model(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.ADABoostRegression(random_state=2, run=True)

        model.ada_reg.to_pickle()

        validate = os.path.exists(str(Path.home()) + "/.aethos/models/ada_reg.pkl")

        self.assertTrue(validate)

    def test_pickle_model_analysis(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Regression(x_train=data, target="col3")
        model.ADABoostRegression(random_state=2, run=True)

        model.to_pickle("ada_reg")

        validate = os.path.exists(str(Path.home()) + "/.aethos/models/ada_reg.pkl")

        self.assertTrue(validate)

    def test_model_create_service(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        model.LogisticRegression(random_state=2, run=True)

        model.to_service("log_reg", "test")

        self.assertTrue(True)

    def test_model_analysis_create_service(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3")
        m = model.LogisticRegression(random_state=2)

        m.to_service("test1")

        self.assertTrue(True)

    def test_list_models_empty(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)

        model.list_models()

        self.assertTrue(True)

    def test_list_models(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l1", run=False
        )
        model.LogisticRegression(
            random_state=2, penalty="l2", model_name="l2", run=True
        )

        model.list_models()

        self.assertTrue(True)

    def test_incorrect_model_name(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)

        self.assertRaises(
            AttributeError,
            model.LogisticRegression,
            random_state=2,
            penalty="l2",
            model_name="x_train",
            run=False,
        )

    def test_model_debug(self):

        data = np.random.randint(0, 2, size=(500, 3))

        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        model = Classification(x_train=data, target="col3", test_split_percentage=0.5,)

        model.help_debug()

        self.assertTrue(True)

    def test_pretrained_sent(self):

        data = [
            "",
            "I'm very excited to be here :).",
            "I'm not very excited to be here.",
        ]

        data = pd.DataFrame(data, columns=["text"])

        df = Unsupervised(data)
        df.pretrained_sentiment_analysis("text")

        validate = df["sent_score"][0][0]

        self.assertIsInstance(validate, dict)

    def test_pretrained_qa(self):

        data = {
            "context": [
                "Pipeline have been included in the huggingface/transformers repository.",
                "hello",
            ],
            "question": ["What is the name of the repository ?", "Is anything here?"],
        }

        data = pd.DataFrame(data)

        df = Unsupervised(data)
        df.pretrained_question_answer("context", "question")

        validate = df["qa"][0]

        self.assertIsInstance(validate, dict)


if __name__ == "__main__":
    unittest.main()
