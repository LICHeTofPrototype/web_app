//
//  ViewController.swift
//  HHH
//
//  Created by Kojiro Machi on 2020/02/01.
//  Copyright © 2020 LICHeT. All rights reserved.
//

import UIKit
import HealthKit



class ViewController: UIViewController {
    
    let store = HKHealthStore()
    
    let readTypes = Set([
        HKWorkoutType.workoutType(),
        HKQuantityType.quantityType(forIdentifier: HKQuantityTypeIdentifier.heartRate)!
    ])
    
    let writeTypes = Set([
        HKQuantityType.quantityType(forIdentifier: HKQuantityTypeIdentifier.heartRate)!
    ])
    
//*******************************************
//権限のリクエストを行う
//*******************************************
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        store.requestAuthorization(toShare: nil, read: readTypes, completion: { success, error in
            if success {
                print("Success")
            } else {
                print("Error")
            }
        })
    }

        
//*******************************************
//権限のリクエストを行う
//*******************************************
    
func getHeartRate(){
    // 取得する期間を設定
    let dateformatter = DateFormatter()
    dateformatter.dateFormat = "yyyy/MM/dd"
    let startDate = dateformatter.date(from: "2020/01/01")
    let endDate = dateformatter.date(from: "2020/01/31")
    
    // 取得するデータを設定
    let typeOfHR = HKObjectType.quantityType(
        forIdentifier: HKQuantityTypeIdentifier.heartRate
    )
    
    let statusOptions: HKStatisticsOptions = [
        HKStatisticsOptions.discreteMin,
        HKStatisticsOptions.discreteMax
    ]
    
    let predicate = HKQuery.predicateForSamples(
        withStart: startDate,
        end: endDate,
        options: HKQueryOptions.strictStartDate
    )
    
    let query = HKStatisticsQuery(
        quantityType: typeOfHR!,
        quantitySamplePredicate: predicate,
        options: statusOptions,
        completionHandler: { (query, result, error) in
            if let e = error {
                print("Error: \(e.localizedDescription)")
                return
            }
            DispatchQueue.main.async {
                guard let r = result else {
                    print("Result")
                    return
                }
            let min = r.minimumQuantity()
            let max = r.maximumQuantity()
            if min != nil && max != nil {
                    print("\(r.startDate) : \(r.endDate) 最小:\(min!) 最大:\(max!)")
                }
            }
        })
    store.execute(query)
    }

    @IBAction func tap(_ sender: Any) {
        getHeartRate()
    }
    
}
